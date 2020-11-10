# import Flask and PyMongo and scraping code,
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scraping

# set up Flask:
app = Flask(__name__)
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# define the route for the HTML page.
# Flask what to display when we're looking at the home page
@app.route("/")
#define function 
def index():
    # uses PyMongo to find the "mars" collection in our database,
    mars = mongo.db.mars.find_one()
    #return an HTML template using an index.html 
    return render_template("index.html", mars=mars)

# function will set up our scraping route
#1.defines the route that Flask will be using.
@app.route("/scrape")
# define function
def scrape():
    # assign a new variable that points to our Mongo database mongo.db.mars
    mars = mongo.db.mars
    # created a new variable to hold the newly scraped data
    mars_data = scraping.scrape_all()
    # update the database using .update(), 
    # add an empty JSON object with {},stored in mars_data, option upsert=True
    mars.update({}, mars_data, upsert=True)
    # add a message to let us know that the scraping was successful
    return "Scraping Successful!"

# final code we need for Flask to run.
if __name__ == "__main__":
   app.run()



