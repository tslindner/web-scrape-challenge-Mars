
# coding: utf-8

# In[1]:

# import dependencies
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from splinter import Browser


# In[2]:


# 1 = NASA Mars News
# 2 = JPL Mars Space Images
# 3 = Mars Weather
# 4 = Mars Facts
# 5 = Mars Hemispheres


# In[3]:


url1 = "https://mars.nasa.gov/news/"
url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
url3 = "https://twitter.com/marswxreport?lang=en"
url4 = "https://space-facts.com/mars/"
url5 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"


# In[4]:


def soupify(url):
    browser = Browser("chrome")
    browser.visit(url)
    html_code = browser.html
    soup = bs(html_code, "html.parser")
    return soup
    browser.windows[0].close()
    

def scrape():
    
    soup1 = soupify(url1)
    soup2 = soupify(url2)
    soup3 = soupify(url3)
    soup4 = soupify(url4)
    soup5 = soupify(url5)


    # In[5]:


    # 1 Mars news


    # In[6]:


    news_title = soup1.find("div", class_="content_title").text.strip()
    news_p = soup1.find("div", class_="article_teaser_body").text.strip()


    # In[7]:


    # 2 JPL featured image


    # In[8]:


    featured_image_url = soup2.find("article", class_="carousel_item")


    # In[9]:


    featured_image_url = featured_image_url['style'][23:-3]


    # In[10]:


    featured_image_url = "https://www.jpl.nasa.gov" + featured_image_url


    # In[11]:


    # 3 Mars weather


    # In[12]:


    mars_weather = soup3.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    

    # In[13]:


    # 4 Mars facts


    # In[14]:


    mars_facts_dict = {}


    # In[15]:


    mars_facts = soup4.find_all("table", class_="tablepress tablepress-id-mars")[0].find_all("tr")


    # In[16]:


    for i in range(len(mars_facts)):

        field = mars_facts[i].find_all("td")[0].text.strip()
        value = mars_facts[i].find_all("td")[1].text.strip()

        field = field.replace(" ", "_")
        field = field[:-1]



        mars_facts_dict[field] = value

    

    # In[19]:


    # 5 Mars hemispheres


    # In[27]:


    hemi_image_urls = []

    hemi_base_url = "https://astrogeology.usgs.gov"

    hemi_exts = soup5.find_all("div", class_="description")

    for ext in hemi_exts:
        loop_dict = {}

        hemi_title = ext.a.text[:-9]

        hemi_ext = ext.a["href"]
        hemi_url_1 = hemi_base_url + hemi_ext

        hemi_soup = soupify(hemi_url_1)
        hemi_url_2 = hemi_soup.find("div", class_="downloads").a["href"]

        loop_dict["title"] = hemi_title
        loop_dict["img_url"] = hemi_url_2

        hemi_image_urls.append(loop_dict)


    # In[28]:


    results = {}
    results["news_title"] = news_title
    results["news_p"] = news_p
    results["featured_image_url"] = featured_image_url
    results["mars_weather"] = mars_weather
    results["facts"] = mars_facts_dict
    results["hemi_image_urls"] = hemi_image_urls
    results["hemi_0"] = hemi_image_urls[0]
    results["hemi_1"] = hemi_image_urls[1]
    results["hemi_2"] = hemi_image_urls[2]
    results["hemi_3"] = hemi_image_urls[3]

        
        
    return results

