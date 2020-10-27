from flask import Flask, render_template

# import pymongo library, and connect flask app to database
from flask_pymongo import PyMongo
import scrape_mars

#Create an instance of our Flask app
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymono instance
client = pymongo.MongoClient(conn)

# Connect to database created in pgadmin
db = client.Web_Scraping_Challenge



