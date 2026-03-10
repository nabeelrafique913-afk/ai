from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

url = 'https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094'

cService = webdriver.ChromeService(executable_path='C:\\Users\\GEO\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=cService)

driver.get(url)
qouestList=[]
qoutesDiv = driver.find_elements(By.XPATH, "//div[contains(@class, 'carousel__viewport carousel__viewport--mask')]")
for p in range(len(qoutesDiv) -1):
    quote = {}
    innerImg = qoutesDiv[p+1].find_element(By.TAG_NAME, "img")
    innera = qoutesDiv[p+1].find_element(By.TAG_NAME, "a")
    quote["img"] =innerImg.get_attribute('class') 
    quote["lines"] =innerImg.get_attribute('loading') 
    quote["aurthor"] =innerImg.get_attribute('alt')
    quote["data-src"] =innerImg.get_attribute('data-src')
    quote["a"] =innera.get_attribute('data-interactions')
    quote["sp"] =innera.get_attribute('_sp')
    quote["href"] =innera.get_attribute('href')
    qouestList.append(quote)

filename = 'nabeel/ebaySSS_quotesMethod3.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['img','lines','aurthor','data-src','a','sp','href'])
    w.writeheader()
    for quote in qouestList:
        w.writerow(quote)

driver.close()
