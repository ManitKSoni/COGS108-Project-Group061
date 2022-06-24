import requests
import os.path
import pandas as pd
import requests, re
import bs4
from bs4 import BeautifulSoup


# Each of these URLS lists more URLS that pertain to politics of that month
monthList = []

articles = []

for i in range(1,9):
  monthList.append("https://www.breitbart.com/tag/2016-presidential-election/page/"+str(i)+"/")
                   
# Iterate through each of those months and get every URL
for url in monthList:
    website = requests.get(url)
    soup = BeautifulSoup(website.content, 'html.parser')
    entries = soup.find_all("article");

    
    for article in entries:
        a = article.find("a")
        articles.append("https://www.breitbart.com" + a['href'])

#write these links to a file
f = open("Files/2016BreitbartArticleURLS.txt", "w")
for url in articles:
    f.write(url + "\n")
f.close()
