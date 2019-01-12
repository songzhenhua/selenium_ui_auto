#coding=utf-8

from selenium import webdriver

# 设置下载目录
options = webdriver.ChromeOptions()
prefs = {'download.default_directory': 'd:\\'}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(executable_path='D:\\szh\\autoui_ddc2\\driver\\chromedriver.exe', chrome_options=options)
driver.get('http://sahitest.com/demo/saveAs.htm')
driver.find_element_by_xpath('//a[text()="testsaveas.zip"]').click()
sleep(3)
driver.quit()