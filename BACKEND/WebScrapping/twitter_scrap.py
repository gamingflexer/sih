import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import hashlib

# PATH to chrome driver
PATH = 'D:\\Softwares\\chromedriver.exe'
ser = Service(PATH)
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.implicitly_wait(1)
driver.maximize_window()

USERNAME = 'adwaitswim@gmail.com'
PHONE = ''
PASS = ''

driver.get('https://twitter.com/i/flow/login')
time.sleep(7)

# TODO : Login Into Account

# Enter Username
driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input').send_keys(USERNAME)
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]').click()

time.sleep(2)

# Enter Phone
driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input').send_keys(PHONE)
driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div').click()
time.sleep(5)

# Enter Password
driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(PASS)


time.sleep(5)

# TODO : Insert #tags into search bar

# TODO : Get the tweets and keep them seperated Try to get images from tweets

# TODO : Store data in JSON format

driver.quit()
