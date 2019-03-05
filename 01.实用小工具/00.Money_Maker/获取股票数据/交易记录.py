#!/usr/bin/python
#coding=utf-8

import sys
from selenium import webdriver

reload(sys)
sys.setdefaultencoding('utf-8')

driver = webdriver.PhantomJS(executable_path='C:\Python27\Scripts\phantomjs-2.1.1-windows\phantomjs.exe')
driver.get("http://www.baidu.com")
data = driver.title
print (data)
