from splinter import Browser
from bs4 import BeautifulSoup

def init_browser():
    executable_path = {"executable_path": "C:/Users/Cory/Downloads/chromedriver_win32/chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    # Visit first url