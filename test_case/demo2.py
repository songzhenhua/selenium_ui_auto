# coding=utf-8
# @Time  : 2019/12/22
# @Author: 星空物语
# @File  : demo2.py
# @Description: 自己测试用，无效文件


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 使用已打开的Chrome浏览器进行调试
# 首先使用命令打开Chrome浏览器并开启远程调试功能
# chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\code\python\selenium_ui_auto\chrome_temp"
# 手动打开百度首页，以下代码可以执行成功

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = r"D:\code\python\selenium_ui_auto\driver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

driver.find_element_by_id('kw').send_keys(u'测试工程师小站')