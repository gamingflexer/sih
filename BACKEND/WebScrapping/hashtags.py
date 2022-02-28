import re
import time
from socket import socket
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import wget


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(executable_path="/Users/cosmos/98", chrome_options=chrome_options)  

t1 = "#india" 
t2 = "#naturaldisaster" 
t3 = "#disaster" 
t4 = "#emergency" 

d1 = "#flood"
d2 = "#earthquake" 
d3 = "#fire" 
d4 = "#wildfire" 
d5 = "#huricane" 


class hashtags():
    def __init__(self,h1,h2,h3,h4,h5):
        self.h1 = h1
        self.h2 = h2
        self.h3 = h3
        self.h4 = h4
        self.h5 = h5

    
    def add(self):
        driver.get("https://displaypurposes.com/")
        time.sleep(2)
        
        elemUser = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/input")
        elemUser.send_keys(self.h1)
        elemUser.send_keys(self.h2)
        elemUser.send_keys(self.h3)
        elemUser.send_keys(self.h4)
        elemUser.send_keys(self.h5)
        time.sleep(5)
    
    def save(self):
         savehashtags=driver.find_element_by_xpath('//*[@id="app"]/div/div/div[3]/div[2]/div/button')
         savehashtags.click()
         newtags = driver.find_element_by_xpath('/html/body/div[2]/div').text
         return newtags


        
#Create an object
scrape = hashtags(t1,t2,t3,t4,d1)
scrape.add()
final_tags = scrape.save()
driver.quit()

print(final_tags)