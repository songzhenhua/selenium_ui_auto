# coding=utf-8
# @Time  : 2019/12/22
# @Author: 星空物语
# @File  : conftest.py
# @Description: 1.pytest提供数据、操作共享的文件
#               2.conftest.py文件名是固定的，不可以修改
#               3.conftest.py文件所在目录必须存在__init__.py文件
#               4.其他文件不需要import导入conftest.py，pytest用例会自动查找
#               5.所有同目录测试文件运行前都会执行conftest.py文件

import pytest
from selenium import webdriver


# def setup_module():
# """
# 初始化selenium webdriver，默认为chromedriver
# :param browser: chrome,firefox/ff
# """
# browser = browser.lower()
# if browser == 'firefox' or browser == 'ff':
#     driver = webdriver.Firefox()
# else:
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('--start-maximized')  # 浏览器最大化
#     chrome_options.add_argument('--disable-infobars')  # 不提醒chrome正在受自动化软件控制
#     prefs = {'download.default_directory': 'd:\\'}
#     chrome_options.add_experimental_option('prefs', prefs)  # 设置默认下载路径
#     # chrome_options.add_argument(r'--user-data-dir=D:\ChromeUserData')  # 设置用户文件夹，可免登陆
#     driver = webdriver.Chrome('D:\\code\\python\\selenium_ui_auto\\driver\\'+'chromedriver.exe', options=chrome_options)
# try:
#     self.driver = driver
# except Exception, e:
#     raise e
#
#
# def teardown_module():
#     driver.quit()
# driver = None
#
#
# @pytest.fixture(scope='session')
# def driver():
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('--start-maximized')  # 浏览器最大化
#     chrome_options.add_argument('--disable-infobars')  # 不提醒chrome正在受自动化软件控制
#     prefs = {'download.default_directory': 'd:\\'}
#     chrome_options.add_experimental_option('prefs', prefs)  # 设置默认下载路径
#     # chrome_options.add_argument(r'--user-data-dir=D:\ChromeUserData')  # 设置用户文件夹，可免登陆
#     global driver
#     driver = webdriver.Chrome('D:\\code\\python\\selenium_ui_auto\\driver\\'+'chromedriver.exe', options=chrome_options)
#     yield driver
#     driver.quit()