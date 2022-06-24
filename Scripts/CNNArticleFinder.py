import requests
import os.path
import pandas as pd
import requests, re
import bs4
from bs4 import BeautifulSoup


# Each of these URLS lists more URLS that pertain to politics of that month
monthList = [
    "https://www.cnn.com/politics/article/sitemap-2016-1.html", #January
    "https://www.cnn.com/politics/article/sitemap-2016-2.html", #February
    "https://www.cnn.com/politics/article/sitemap-2016-3.html", #March
    "https://www.cnn.com/politics/article/sitemap-2016-4.html", #April
    "https://www.cnn.com/politics/article/sitemap-2016-5.html", #May
    "https://www.cnn.com/politics/article/sitemap-2016-6.html", #June
    "https://www.cnn.com/politics/article/sitemap-2016-7.html", #July
    "https://www.cnn.com/politics/article/sitemap-2016-8.html", #August
    "https://www.cnn.com/politics/article/sitemap-2016-9.html", #September
    "https://www.cnn.com/politics/article/sitemap-2016-10.html", #October
    "https://www.cnn.com/politics/article/sitemap-2016-11.html", #November
    "https://www.cnn.com/politics/article/sitemap-2016-12.html", #December
]

articles = []

# Iterate through each of those months and get every URL
for url in monthList:
    website = requests.get(url)
    soup = BeautifulSoup(website.content, 'html.parser')
    entries = soup.find_all("span", class_="sitemap-link");
    
    #Remove that first element because it is extraeneous
    entries.remove(entries[0])
    
    for span in entries:
        a = span.find("a")
        articles.append(a['href'])

#write these links to a file
f = open("Files/2016CNNArticleURLS.txt", "w")
for url in articles:
    f.write(url + "\n")
f.close()
