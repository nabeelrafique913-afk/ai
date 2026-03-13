from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

url = "https://www.zameen.com/Homes/Lahore-1-1.html"

cService = webdriver.ChromeService(executable_path='C:\\Users\\GEO\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe') # '/Users/bpfalz/Downloads/chromedriver' for my macbook
driver = webdriver.Chrome(service=cService)

driver.get(url)

qouestList=[]

qoutesDiv = driver.find_elements(By.XPATH, "//div[contains(@class, '_2a2e3d21')]")

for p in range(len(qoutesDiv) -1):
    quote = {}
    innerImg = qoutesDiv[p+1].find_element(By.TAG_NAME, "a")
    quote["href"] =innerImg.get_attribute('href') 
    quote["title"] =innerImg.get_attribute('title') 
    qouestList.append(quote)

    filename = 'nabeel/inspirational_zameenMethod2.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['a','href','title'])
    w.writeheader()
    for quote in qouestList:
        w.writerow(quote)

driver.close()