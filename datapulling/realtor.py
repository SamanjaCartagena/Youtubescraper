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





my_list=[]
with open('C:\\Users\\c.samanja09\\Desktop\\numbers.csv','r', encoding='ANSI') as file:
       reader = csv.DictReader(file)
       columnNames = reader.fieldnames
       for row in reader:
          driver.get("https://www.youtube.com/")
          time.sleep(3)

          driver.maximize_window()

          search=driver.find_elements(By.TAG_NAME,"input")

          search[0].click()
          full_name=row['First Name']+" "+row['Last Name']
          info=row['First Name']+","+row['Last Name']+","+row['Email Address']+","+row['Company Name']+","+row['Phone Number']
          search[0].send_keys(full_name)

          btn=driver.find_element(By.XPATH,"//button[@aria-label='Search']").click()
          time.sleep(10)

          found=driver.find_elements(By.XPATH,'//*[contains(text(), "' + full_name + '")]')
          
          realtor=driver.find_elements(By.XPATH,"//*[contains(text(), 'real estate')]")
          time.sleep(5)
          
          if len(found)>5 and len(realtor)>5:
              print(full_name+'YouTube account exists')
              print(len(found))
              print(len(realtor))
              new_file=open('youtube.csv','a',newline='')
              writer=csv.writer(new_file)
              writer.writerows(info)
              
          else:
              print('No')

         
    





'''


d=['Sam',"Cartagena",'cart.sam@gmail.com']



data_append=[
    ['Janet','Canada','janet@yahoo.com'],
    ['Pierre','France','pierre@gmail.com']
    ]
data_append.append(d)
file=open('name.csv','a',newline='')
writer=csv.writer(file)
writer.writerows(data_append)
file.close()

'''