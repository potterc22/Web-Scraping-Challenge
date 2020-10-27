from flask import Flask, render_template

# import pymongo library, and connect flask app to database
from flask_pymongo import PyMongo
import scrape_mars

#Create an instance of our Flask app
app = Flask(__name__)

# use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mission_to_mars_app")

# Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.
@app.route("/")
def index():
    # find the first thing it finds in the database
    mars_info = mongo.db.mars_info.find_one()
    return render_template("index.html", mars_info = mars_info)

# Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.
# Store the return value in Mongo as a Python dictionary.
@app.route("/scrape")
def scraper():
    mars_info = mongo.db.mars_info


if __name__ == "__main__":
    app.run(debug=True)