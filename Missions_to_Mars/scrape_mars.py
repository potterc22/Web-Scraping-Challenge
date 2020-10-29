from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time

def init_browser():
    executable_path = {"executable_path": "C:/Users/Cory/Downloads/chromedriver_win32/chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_info = {}
    # NASA Mars News
    # Visit first url
    url1 = "https://mars.nasa.gov/news/"
    browser.visit(url1)
    time.sleep(2)
    # Declare dependent variables
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    # scrape for the latest news title and paragraph text
    mars_info['news_title'] = soup.find('ul', class_='item_list').\
    find('div', class_='content_title').a.text
    mars_info['news_p'] = soup.find('ul', class_='item_list').\
    find('div', class_='article_teaser_body').text

    # JPL Mars Space Images - Featured Image
    # Visit second url
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)
    # Declare dependent variables
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    # scrape for the JPL featured space image relative url
    relative_url = soup.find('ul', class_='articles').\
    find('a', class_='fancybox')['data-fancybox-href']
    # Declare the base_url variable and add the relative_url to it for the full image url
    base_url = 'https://www.jpl.nasa.gov'
    mars_info['featured_image_url'] = base_url + relative_url

    # Mars Facts
    # use pandas to scrape the Mars Facts webpage for the table containing facts about Mars
    url3 = 'https://space-facts.com/mars/'
    table = pd.read_html(url3)
    # save the first table into a variable
    mars_facts_df = table[0]
    # rename column headings
    mars_facts_df.columns = ['', 'Mars']
    # set the index of the dataframe
    mars_facts_df.set_index('', inplace=True)
    # convert df to html and save to resources folder
    mars_facts = mars_facts_df.to_html(header=True, index=True)
    mars_info['mars_facts'] = mars_facts

    # Mars Hemispheres
    # visit fourth url
    url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url4)
    # Declare dependent variables
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # scrape high resolution images for each of Mar's hemispheres
    # retrieve the parent divs for all hemisphere
    hemispheres = soup.find_all('div', class_='item')
    base_url = 'https://astrogeology.usgs.gov'
    hemisphere_image_urls = []
    # loop over hemispheres to save image details
    for hemisphere in hemispheres:
        # scrape the title
        title = hemisphere.img['alt']
        # scrape the link to the full image, then visit that page
        relative_url = hemisphere.a['href']
        target = base_url + relative_url
        browser.visit(str(target))
        time.sleep(4)
        # re-declare our dependent variables
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        # save the image url to a variable
        downloads = soup.find('img', class_='wide-image')
        relative_url = downloads['src']
        img_url = base_url + relative_url
        # create dictionary to hold hemisphere image details
        hem_dict = {
            "title": title,
            "img_url": img_url
        }
        # append dictionary to list
        hemisphere_image_urls.append(hem_dict)
    # add the list of dictionaries to the mars_info dictionary
    mars_info['hemisphere_img'] = hemisphere_image_urls

    # close browser after scraping
    browser.quit()
    # return results
    return mars_info
