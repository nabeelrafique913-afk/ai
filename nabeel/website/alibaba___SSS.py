from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

url = 'https://www.alibaba.com/trade/search?spm=a2700.product_home_newuser.header.132.2ce267afSeLPmg&SearchText=Auto+Accessories&indexArea=product_en&search_cource_scene=pc_home_product_category&has4Tab=true&tab=all'

cService = webdriver.ChromeService(executable_path='C:\\Users\\GEO\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=cService)

driver.get(url)
qouestList=[]
qoutesDiv = driver.find_elements(By.XPATH, "//div[contains(@class, 'searchx-product-e-slider__wrapper')]")
for p in range(len(qoutesDiv) -1):
    quote = {}
    innerImg = qoutesDiv[p+1].find_element(By.TAG_NAME, "a")
    innera = qoutesDiv[p+1].find_element(By.TAG_NAME, "img")
    quote["url"] =innerImg.get_attribute('href') 
    quote["search"] =innerImg.get_attribute('class') 
    quote["item"] =innerImg.get_attribute('target')
    quote["image_item"] =innerImg.get_attribute('data-spm')
    quote["card"] =innerImg.get_attribute('data-aplus-auto-card-mod')
    quote["anchor_id"] =innerImg.get_attribute('data-spm-anchor-id')
    quote["data-aplus-ae"] =innerImg.get_attribute('data-aplus-ae')
    quote["img"] =innera.get_attribute('src')
    quote["class"] =innera.get_attribute('class')
    qouestList.append(quote)

filename = 'nabeel/alibaba__SS_quotesMethod3.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['url','search','item','image_item','card','anchor_id','data-aplus-ae','img','class'])
    w.writeheader()
    for quote in qouestList:
        w.writerow(quote)

driver.close()
