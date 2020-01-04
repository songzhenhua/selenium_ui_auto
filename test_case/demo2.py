# coding=utf-8
# @Time  : 2019/12/22
# @Author: 星空物语
# @File  : demo1.py
# @Description: 自己测试用，无效文件

from selenium import webdriver

# 设置下载目录
options = webdriver.ChromeOptions()
prefs = {'download.default_directory': 'd:\\'}
options.add_experimental_option('prefs', prefs)
options.add_argument('--disable-infobars')  # 不提醒chrome正在受自动化软件控制
driver = webdriver.Chrome(executable_path='D:\\code\\python\\selenium_ui_auto\\driver\\chromedriver.exe', chrome_options=options)
# driver.get('http://sahitest.com/demo/saveAs.htm')
# driver.find_element_by_xpath('//a[text()="testsaveas.zip"]').click()
driver.get('http://www.baidu.com')


# driver.quit()