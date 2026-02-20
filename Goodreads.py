from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.goodreads.com/list/show/12362.All_Time_Favorite_Romance_Novels?page=1')
content = driver.page_source
soup = bs(content)
print(soup)



