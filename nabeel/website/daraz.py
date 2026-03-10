#Python program to scrape website 
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.daraz.pk/catalog/?spm=a2a0e.tm80331704.cate_5.5.77cc5aa7fPImi7&q=Smart%20Phones&from=hp_categories&src=all_channel"
r = requests.get(URL)
 
soup = BeautifulSoup(r.content, 'html5lib')
 
quotes=[]  # a list to store quotes
 
table = soup.find('div', attrs = {'data-spm-anchor-id':'a2a0e.searchlist.list.i0.1afc6b3eT8pzsn'}) 
print(table)

for row in table.find_all('div',
                         attrs = {'class':'_Y29ud_bxcGridColumn_J5gfU _Y29ud_bxcGridColumn1Of5_UoKNf'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['alt']
    quote['lines'] = row.img['src'].split(" ")[0]
    quote['author'] = row.img['src'].split(" ")[1]
    quotes.append(quote)