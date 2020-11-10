# Mission-to-Mars/Web_Scrpting

## Background

Navigate a web browser automatively to extract data about the Mission to Mars and store it in a NoSQL
database, and then render the data in a web application created with Flask. 
The collected work will be displayed in HTML web browser. 

### Goals:

- Use HTML elements, class and id attributes, to identify content for web scraping.
- Use BeautifulSoup and Splinter to automate a web browser and perform a web scrape.
- Create a MongoDB database to store data from the web scrape.
- Create a web application with Flask to display the data from the web scrape.
- Create an HTML/CSS portfolio to showcase projects.
- Use Bootstrap components to polish and customize the portfolio.

### Resources:

- NonSQL database (MongoDB), HTML editer (VS code)
- Web Scraping Tools (ChromeDriver, Splinter and BeautifulSoup)
- Scrape sites (url): https://mars.nasa.gov/news
- https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
- http://space-facts.com/mars/
- https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
                      
                      

## Major Outputs:

### Step 1 - Scraping

#### Scrape Mars Data: The News

* Scrape data from the NASA Mars News Site and collect the latest News Title and Paragraph Text
 - Visit the mars NSAS news site, url = 'https://mars.nasa.gov/news/'
 - Set up the HTML parser:
 - Find and assign the title and summary text to variables
 - Scrap website title and text.
 
#### Scrape Mars Data: Featured Image

* Visit the URL for the JPL Featured Space Image,  url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
* Use Splinter to navigate the site and find the image URL for the current Featured Mars Image and assign the URL string to a variable called `featured_image_url`
* Make sure to find the image URL to the full size `.jpg` image
* Make sure to save a complete URL string for this image

#### Scrape Mars Data: Mars Facts

* Visit the Mars Facts webpage, url = 'https://space-facts.com/mars/'
* Scrape the table containing facts about the planet including Diameter, Mass, etc.
* Use Pandas to convert the data to a HTML table string


### Step 2 - MongoDB and Flask Application

* Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above
* Convert Jupyter Notebook into a Python Script called `scrape_mars.py` with a function called `scrape` that will execute all of the scraping code from above and return one Python Dictionary containing all of the scraped data
* Create a route called `/scrape` that will import the `scrape_mars.py` script and call the `scrape` function
    * Store the return value in Mongo as a Python Dictionary
* Create a root route `/` that will query the Mongo database and pass the Mars Data into an HTML template to display the data
* Create a template HTML file called `index.html` that will take the Mars Data Dictionary and display all of the data in the appropriate HTML elements


# Challenge

### Background

 - Scraping of four images of Mars’s hemispheres from the search results of Mars. we will adjust the current web app to include all four of the hemisphere images: Cerberus Hemisphere, Schiaparelli Hemisphere, Syrtis Major Hemisphere, Valles Marineris Hemisphere.
- url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

### Goals

* Using BeautifulSoup and Splinter, you’ll scrape full-resolution images of Mars’s hemispheres and the titles of those images.
* Update the Web App with Mars Hemisphere Images and Titles
* Update your web app to make it mobile- responsive, and add two additional Bootstrap 3 components to make it
stand out.



### Challenge Outputs:

1. Pandas code that retrieves the url of the full-resolution image and title for each hemisphere image
 
  -Jupyter NoteBooks [ETL_function_test.ipynb](ETL_function_test.ipynb) and Python script [challenge.py](Pyscirpt/ETL_function_test.py)

2. The list contains the dictionary of the full-resolution image URL string and title for each hemisphere image.  

  -Jupyter NoteBooks [ETL_clean_wiki_movies.ipynb](ETL_clean_wiki_movies.ipynb) and Python script [ETL_clean_wiki_movies.py](Pyscirpt/ETL_clean_wiki_movies.py)

3. The scraping.py code for retriveing the full-resolution image URL and title for each hemisphere image (10 pt)

-Jupyter NoteBooks [ETL_clean_kaggle_data.ipynb](ETL_clean_kaggle_data.ipynb) and Python script [ETL_clean_kaggle_data.py](Pyscirpt/ETL_clean_kaggle_data.py)

4. Update the Mongo database and represent the index.html that display the full-resolution image URL and title for each hemisphere image

[ETL_create_database.ipynb](ETL_create_database.ipynb) and Python script [ETL_create_database.py](Pyscirpt/ETL_create_database.py)

https://htmlpreview.github.io/?https://github.com/sbaik97/Mission-to-Mars-Web_Scrpting/blob/main/templates/Mission%20to%20Mars.html
5. Update the index.html file so your website is mobile-responsive.

- Elapsed time to add the data to the database

![elapsed_time.PNG](Resources/elapsed_time_for_upload.PNG)


### Conclusions
- Creating a function is more effective way to extract, transform and load process to a PostgreSQL database for large datafile.
- From ETL process we can collect, clean, and uploade the data into the sql server. Importing a rating data takes quite a long time (3572.5107519626617 seconds) and  it's helpful to see the time information.



