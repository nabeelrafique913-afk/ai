#Python program to scrape website 
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.amazon.com/gp/browse.html?node=6563140011&ref_=nav_em_amazon_smart_home_0_2_8_2"
r = requests.get(URL)
 
soup = BeautifulSoup(r.content, 'html5lib')
 
quotes=[]  # a list to store quotes
 
table = soup.find('div', attrs = {'id':'0'}) 
print(table)

for row in table.find('div',
                         attrs = {'class':'_Y29ud_bxcGridImage_mukPG _Y29ud_bxcGridHalign_3QrYc _Y29ud_bxcGridHalignCenter_YYl_I'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['alt']
    quote['img1'] = row.img['src']
    quote['lines'] = row.img['src'].split(" ")[0]
    quote['author'] = row.img['src'].split(" ")[1]
    quotes.append(quote)
 
filename = 'nabeel/amazonBS.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['theme','url','img','img1','lines','author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)