#Python program to scrape website 
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.zameen.com/Homes/Lahore-1-1.html"
r = requests.get(URL)
 
soup = BeautifulSoup(r.content, 'html5lib')
 
quotes=[]  # a list to store quotes
 
table = soup.find('div', attrs = {'class':'_5b98ebdf'}) 
print(table)

for row in table.find('div',
                         attrs = {'class':'_2a2e3d21'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['alt']
    quote['lines'] = row.img['src'].split(" ")[0]
    quote['author'] = row.img['src'].split(" ")[1]
    quotes.append(quote)
 