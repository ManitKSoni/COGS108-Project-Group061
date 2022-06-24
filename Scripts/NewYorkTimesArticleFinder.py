import requests
import os.path
import pandas as pd
import requests, re
import bs4
from bs4 import BeautifulSoup


# Each of these URLS lists more URLS that pertain to politics of that month
monthList = []

#june
for i in range(1,31):
    if(i < 10):
        monthList.append("https://www.nytimes.com/search?dropmab=true&endDate=201606"+"0"+str(i)+"&query=2016%20election&sections=U.S.%7Cnyt%3A%2F%2Fsection%2Fa34d3d6c-c77f-5931-b951-241b4e28681c&sort=best&startDate=201606"+"0"+str(i)+"&types=article");
    else:
        monthList.append("https://www.nytimes.com/search?dropmab=true&endDate=201606"+str(i)+"&query=2016%20election&sections=U.S.%7Cnyt%3A%2F%2Fsection%2Fa34d3d6c-c77f-5931-b951-241b4e28681c&sort=best&startDate=201606"+str(i)+"&types=article");


#july
for i in range(1,32):
    if(i < 10):
        monthList.append("https://www.nytimes.com/search?dropmab=true&endDate=201607"+"0"+str(i)+"&query=2016%20election&sections=U.S.%7Cnyt%3A%2F%2Fsection%2Fa34d3d6c-c77f-5931-b951-241b4e28681c&sort=best&startDate=201607"+"0"+str(i)+"&types=article");
    else:
        monthList.append("https://www.nytimes.com/search?dropmab=true&endDate=201607"+str(i)+"&query=2016%20election&sections=U.S.%7Cnyt%3A%2F%2Fsection%2Fa34d3d6c-c77f-5931-b951-241b4e28681c&sort=best&startDate=201607"+str(i)+"&types=article");

#august
for i in range(1,32):
    if(i < 10):
        monthList.append("https://www.nytimes.com/search?dropmab=true&endDate=201608"+"0"+str(i)+"&query=2016%20election&sections=U.S.%7Cnyt%3A%2F%2Fsection%2Fa34d3d6c-c77f-5931-b951-241b4e28681c&sort=best&startDate=201608"+"0"+str(i)+"&types=article");
    else:
        monthList.append("https://www.nytimes.com/search?dropmab=true&endDate=201608"+str(i)+"&query=2016%20election&sections=U.S.%7Cnyt%3A%2F%2Fsection%2Fa34d3d6c-c77f-5931-b951-241b4e28681c&sort=best&startDate=201608"+str(i)+"&types=article");

#september
for i in range(1,31):
    if(i < 10):
        monthList.append("https://www.nytimes.com/search?dropmab=true&endDate=201609"+"0"+str(i)+"&query=2016%20election&sections=U.S.%7Cnyt%3A%2F%2Fsection%2Fa34d3d6c-c77f-5931-b951-241b4e28681c&sort=best&startDate=201609"+"0"+str(i)+"&types=article");
    else:
        monthList.append("https://www.nytimes.com/search?dropmab=true&endDate=201609"+str(i)+"&query=2016%20election&sections=U.S.%7Cnyt%3A%2F%2Fsection%2Fa34d3d6c-c77f-5931-b951-241b4e28681c&sort=best&startDate=201609"+str(i)+"&types=article");

#october
for i in range(1,32):
    if(i < 10):
        monthList.append("https://www.nytimes.com/search?dropmab=true&endDate=201610"+"0"+str(i)+"&query=2016%20election&sections=U.S.%7Cnyt%3A%2F%2Fsection%2Fa34d3d6c-c77f-5931-b951-241b4e28681c&sort=best&startDate=201610"+"0"+str(i)+"&types=article");
    else:
        monthList.append("https://www.nytimes.com/search?dropmab=true&endDate=201610"+str(i)+"&query=2016%20election&sections=U.S.%7Cnyt%3A%2F%2Fsection%2Fa34d3d6c-c77f-5931-b951-241b4e28681c&sort=best&startDate=201610"+str(i)+"&types=article");

#november
for i in range(1,31):
    if(i < 10):
        monthList.append("https://www.nytimes.com/search?dropmab=true&endDate=201611"+"0"+str(i)+"&query=2016%20election&sections=U.S.%7Cnyt%3A%2F%2Fsection%2Fa34d3d6c-c77f-5931-b951-241b4e28681c&sort=best&startDate=201611"+"0"+str(i)+"&types=article");
    else:
        monthList.append("https://www.nytimes.com/search?dropmab=true&endDate=201611"+str(i)+"&query=2016%20election&sections=U.S.%7Cnyt%3A%2F%2Fsection%2Fa34d3d6c-c77f-5931-b951-241b4e28681c&sort=best&startDate=201611"+str(i)+"&types=article");

#December
for i in range(1,32):
    if(i < 10):
        monthList.append("https://www.nytimes.com/search?dropmab=true&endDate=201612"+"0"+str(i)+"&query=2016%20election&sections=U.S.%7Cnyt%3A%2F%2Fsection%2Fa34d3d6c-c77f-5931-b951-241b4e28681c&sort=best&startDate=201612"+"0"+str(i)+"&types=article");
    else:
        monthList.append("https://www.nytimes.com/search?dropmab=true&endDate=201612"+str(i)+"&query=2016%20election&sections=U.S.%7Cnyt%3A%2F%2Fsection%2Fa34d3d6c-c77f-5931-b951-241b4e28681c&sort=best&startDate=201612"+str(i)+"&types=article");

articles = []

# Iterate through each of those months and get every URL
for url in monthList:
    website = requests.get(url)
    soup = BeautifulSoup(website.content, 'html.parser')
    entries = soup.find_all("div", class_="css-1i8vfl5");

    
    for article in entries:
        a = article.find("a")
        articles.append("https://www.nytimes.com/" + a['href'])

#write these links to a file
f = open("Files/2016NYTimesArticleURLS.txt", "w")
for url in articles:
    f.write(url + "\n")
f.close()
