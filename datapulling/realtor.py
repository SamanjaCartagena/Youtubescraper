# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:30:44 2024

@author: c.samanja09
"""

import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as bs
import datetime

'''
driver = webdriver.Chrome()

driver.get("https://www.youtube.com/")
time.sleep(3)

driver.maximize_window()

search=driver.find_elements(By.TAG_NAME,"input")

search[0].click()

search[0].send_keys('Kevin Ray Ward')

btn=driver.find_element(By.XPATH,"//button[@aria-label='Search']").click()
time.sleep(10)



found=driver.find_elements(By.XPATH,"//*[contains(text(), 'Kevin Ray Ward')]")

realtor=driver.find_elements(By.XPATH,"//*[contains(text(), 'real estate')]")

if len(found)>5 and len(realtor)>5:
    print('Daniel Kosasih exists')
    print(len(found))
    print(len(realtor))
    
else:
    print('No')

'''
with open('C:\\Users\\c.samanja09\\Desktop\\numbers.csv','r', encoding='ANSI') as file:
       reader = csv.DictReader(file)
       columnNames = reader.fieldnames
       for row in reader:
        print(row['First Name']+" "+row['Last Name'])
       with open('names.csv',mode='w') as new_file:
            fieldnames=['First Name','Last Name']
            writer=csv.DictWriter(new_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({"First Name":row['First Name'],"Last Name":row['Last Name']})
     
