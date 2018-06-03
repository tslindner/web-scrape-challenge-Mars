from flask import Flask, render_template
from scrape_mars import *
import pymongo

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.mars_db
collection = db.info

app = Flask(__name__)


@app.route("/scrape")
def scrape():
    results = scrape()
    
    collection.insert_one(results)
    
@app.route("/")
def home():
    

    

if __name__ == '__main__':
    app.run()