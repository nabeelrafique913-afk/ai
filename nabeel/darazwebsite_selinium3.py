from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

url = 'https://www.daraz.pk/catalog/?spm=a2a0e.tm80331704.cate_5.5.77cc5aa7fPImi7&q=Smart%20Phones&from=hp_categories&src=all_channel'

cService = webdriver.ChromeService(executable_path='C:\\Users\\GEO\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=cService)

driver.get(url)
qouestList=[]
qoutesDiv = driver.find_elements(By.XPATH, "//div[contains(@class, 'picture-wrapper jBwCF')]")
for p in range(len(qoutesDiv) -1):
    quote = {}
    innerImg = qoutesDiv[p+1].find_element(By.TAG_NAME, "img")
    quote["img"] =innerImg.get_attribute('src') 
    quote["lines"] =innerImg.get_attribute('alt') 
    quote["aurthor"] =innerImg.get_attribute('style') 
    qouestList.append(quote)

filename = 'nabeel/daraz_quotesMethod3.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['img','lines','aurthor'])
    w.writeheader()
    for quote in qouestList:
        w.writerow(quote)

driver.close()
