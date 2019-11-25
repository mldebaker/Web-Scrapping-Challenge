# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), '..\\..\..\..\Web-Scrapping-Challenge\Missions_to_Mars'))
	print(os.getcwd())
except:
	pass
# %% [markdown]
# # Mission to Mars Web Scrapping Project

# %%
# Import Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd 
from IPython.display import Image
from IPython.core.display import HTML
import time

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = init_browser()
# %%
# Set url and browser
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)


# %%
# Iterate through all pages
    for x in range(1):
        # HTML object
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        # Retrieve title information
        Headers = soup.find(class_="content_title").text
        # Retrieve paragraph information
        Paragraph = soup.find(class_="article_teaser_body").text



    # Set url and browser
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)


# %%
    # Iterate through all pages
    for x in range(1):
        # HTML object
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        # Retrieve Mars Photo
        featured_image_url = soup.findAll(class_='button fancybox')
        # Retrieve Image link
        for link in featured_image_url:
            image = (f"https://www.jpl.nasa.gov{link.get('data-fancybox-href')}")
            print(image)


# %%
    # Set url and browser
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)


# %%
    # Iterate through all pages
    for x in range(1):
        # HTML object
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        # Retrieve Weather Data
        Weather = soup.find(class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text


# %%
    # Set url
    url2 = 'https://space-facts.com/mars/'
    # Retrieve Table
    table = pd.read_html(url2)
    # Read Table
    table
# %%
    # Create Facts Table
    facts = table[0]
    # Assign rows
    facts.row = ['Equatorial Diameter', 'Polar Diameter', 'Mass', 'Moons', 'Orbit Distance', 'Orbit Period', 'Surface Temperature', 'First Record', 'Recorded By']
    # Set Columns
    facts.columns = ['Facts', 'Data']
# %%
    facts_html = facts.to_html()
# %%
    # Set url and browser
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # Click link
    browser.click_link_by_partial_text('Cerberus')


# %%
    # Retrieve Cerberus hemisphere 
    for x in range(1):
        # HTML object
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        # Grab Image 
        featured_image_url2 = soup.findAll(class_="wide-image")
        # Retrieve Image link
        for link in featured_image_url2:
            Cerberus = (f"https://astrogeology.usgs.gov/{link.get('src')}")
            print(Cerberus)
# %%
    # Set url and browser
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # Click Link
    browser.click_link_by_partial_text('Schiaparelli')


# %%
    # Retrieve Schiaparelli hemisphere 
    for x in range(1):
        # HTML object
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        # Grab Image 
        featured_image_url2 = soup.findAll(class_="wide-image")
        # Retrieve Image link
        for link in featured_image_url2:
            Schiaparelli = (f"https://astrogeology.usgs.gov/{link.get('src')}")
            print(Schiaparelli)

# %%
    # Set url and browser
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # Click Link 
    browser.click_link_by_partial_text('Syrtis')


# %%
    # Retrieve Syrtis hemisphere 
    for x in range(1):
        # HTML object
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        # Grab Image 
        featured_image_url2 = soup.findAll(class_="wide-image")
        # Retrieve Image link
        for link in featured_image_url2:
            Syrtis = (f"https://astrogeology.usgs.gov/{link.get('src')}")
            print(Syrtis)

# %%
    # Set url and browser
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # Click Link 
    browser.click_link_by_partial_text('Valles')
# %%
    # Retrieve Valles hemisphere 
    for x in range(1):
        # HTML object
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        # Grab Image 
        featured_image_url2 = soup.findAll(class_="wide-image")
        # Retrieve Image link
        for link in featured_image_url2:
            Valles = (f"https://astrogeology.usgs.gov/{link.get('src')}")
            print(Valles)
# %%
    # Append Hemispheres to Dictionary
    Mars_Data = {
        "Image": image,
        "Facts": facts_html,
        "Weather": Weather,
        "Paragraph": Paragraph,
        "Headers": Headers,
        "Valles": Valles,
        "Cerberus": Cerberus,
        "Schiaparelli": Schiaparelli,
        "Syrtis": Syrtis,
    }


# %%
    # Close the browser after scraping
    browser.quit()

    # Return results
    return Mars_Data



