# This program takes item name and price of all tiers
# Written by Hunter McQuaid on December 13th, 2021 at 8:30am

# Prerequisites
# if running on mac go to your python x.x folder and run the Certificates.command
# (search Certificates.command in finder and run)
# also make sure to add lxml to path by pip install or adding it to library

# imports
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd


# create class to handle urllib being blocked from website
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


# lists to store data
itemName = []
price = []

# this code is causing warning and will eventually need to be replaced
opener = AppURLopener()
response = opener.open("https://www.smitefire.com/smite/items")

# take data and place in parsing tree 'lxml'
soup = BeautifulSoup(response, "lxml")

# for div container with class name god-name, only take text between tags
# add to item name to itemName list
for div in soup.find_all('div',{"class":"god-name"}):
    item = str(div.text)
    itemName.append(item)
print(itemName)

# for span container with class name hiliteY, only take text between tags
# adds cost of item to price list
for span in soup.find_all('span',{"class":"hiliteY"}):
    item = str(span.text)
    price.append(item)
print(price)

# Add items to DataFrame
df = pd.DataFrame(itemName)
df.to_csv('smiteItems.csv', index=False)

# Add prices to DataFrame
df2 = pd.DataFrame(price)
df2.to_csv('smitePrices.csv', index=False)
