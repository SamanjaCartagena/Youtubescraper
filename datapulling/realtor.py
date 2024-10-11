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


driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
time.sleep(3)
driver.maximize_window()

search=driver.find_elements(By.TAG_NAME,"input")

search[0].click()

search[0].send_keys('Tellula Donald')

btn=driver.find_element(By.XPATH,"//button[@aria-label='Search']").click()
time.sleep(10)

found=driver.find_elements(By.XPATH,"//*[contains(text(), 'Tellula Donald')]")

if len(found)>5:
    print('Coding with Samanja exists')
    print(len(found))
    
else:
    print('No')

'''
with open('C:\\Users\\c.samanja09\\Desktop\\numbers.csv','r', encoding='ANSI') as file:
    print(file.read())
    
'''