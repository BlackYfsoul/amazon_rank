import re
import time
import xlrd
from xlutils.copy import copy
from selenium import webdriver



product_file = file('C:/Users/tplink/Desktop/Rank_get_from_amazon/product_list.txt', 'r')


driver = webdriver.Chrome()
driver.get('https://www.amazon.cn/%E5%85%A8%E6%96%B0Kindle%E7%94%B5%E5%AD%90%E4%B9%A6%E9%98%85%E8%AF%BB%E5%99%A8-%E5%8D%87%E7%BA%A7%E5%A4%96%E8%A7%82%E8%AE%BE%E8%AE%A1-%E7%94%B5%E5%AD%90%E5%A2%A8%E6%B0%B4%E6%98%BE%E7%A4%BA%E5%B1%8F-%E4%B8%93%E6%B3%A8%E9%98%85%E8%AF%BB-%E8%88%92%E9%80%82%E6%8A%A4%E7%9C%BC-%E5%86%85%E7%BD%AEWIFI/dp/B0186FESGW/ref=sr_1_2?ie=UTF8&qid=1483587260&sr=8-2&keywords=kindle')
name = driver.find_element_by_css_selector('#center-20_feature_div > table > tbody > tr:nth-child(2) > td:nth-child(2) > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > p')
ds = driver.find_element_by_css_selector('#technical-details-table > tbody > tr:nth-child(1) > td:nth-child(2)')

print name.text.split('\n')
print ds.text.split('\n')
