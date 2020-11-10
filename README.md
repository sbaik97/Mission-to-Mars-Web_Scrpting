# Mission-to-Mars/Web_Scrpting

## Background

Navigate a web browser automatively to extract data about the Mission to Mars and store it in a NoSQL
database, and then render the data in a web application created with Flask. 
The collected work will be displayed in HTML web browser. 

### Goals:

- Create an automated ETL pipeline.
 
- Extract data from multiple sources using Python.

- Clean and transform the data automatically using Pandas and regular expressions.

- Parse data and to transform text into numbers using regular expressions.

- Load new data into existing tables in PostgreSQL

### Resources:


- Web Scraping Tools (ChromeDriver, Splinter and BeautifulSoup)
- Scrape sites (url): https://mars.nasa.gov/news

                      https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
                      
                      http://space-facts.com/mars/
                      
                      https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
                      
                      


## Objectives

### Step 1 - Scraping

#### NASA Mars News

* Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text

#### JPL Mars Space Images - Featured Image

* Visit the URL for the JPL Featured Space Image
* Use Splinter to navigate the site and find the image URL for the current Featured Mars Image and assign the URL string to a variable called `featured_image_url`
* Make sure to find the image URL to the full size `.jpg` image
* Make sure to save a complete URL string for this image

#### Mars Weather

* Visit the Mars Weather Twitter account and scrape the latest Mars Weather Tweet from the page
    * Save the Tweet text for the weather report as a variable called `mars_weather`

#### Mars Facts

* Visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
* Use Pandas to convert the data to a HTML table string

#### Mars Hemispheres

* Visit the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres
* Save both the image URL string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. 
    * Use a Python dictionary to store the data using the keys `img_url` and `title`
* Append the dictionary with the image URL string and the hemisphere title to a list
    * This list will contain one dictionary for each hemisphere

### Step 2 - MongoDB and Flask Application

* Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above
* Convert Jupyter Notebook into a Python Script called `scrape_mars.py` with a function called `scrape` that will execute all of the scraping code from above and return one Python Dictionary containing all of the scraped data
* Create a route called `/scrape` that will import the `scrape_mars.py` script and call the `scrape` function
    * Store the return value in Mongo as a Python Dictionary
* Create a root route `/` that will query the Mongo database and pass the Mars Data into an HTML template to display the data
* Create a template HTML file called `index.html` that will take the Mars Data Dictionary and display all of the data in the appropriate HTML elements


https://htmlpreview.github.io/?https://github.com/sbaik97/Mission-to-Mars-Web_Scrpting/blob/main/templates/Mission%20to%20Mars.html
