# coding=utf-8
# @Time  : 2019/12/22
# @Author: 星空物语
# @File  : demo1.py
# @Description: 自己测试用，无效文件

from selenium import webdriver
import inspect
import time
import sys

# 通过加cookies免登陆，百度登陆2020.5.7验证通过
chrome_driver = r"D:\code\python\selenium_ui_auto\driver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver)
driver.maximize_window()
driver.get('http://www.baidu.com/')
driver.add_cookie({'name': 'BAIDUID', 'value': '67F332038A56CC0A9B109728BC718D8B'})
driver.add_cookie({'name': 'BIDUPSID', 'value': '67F332038A56CC0A9B109728BC718D8B'})
driver.add_cookie({'name': 'H_PS_PSSID', 'value': '1423_31325_21099_31428_31341_31270_31463_30823_31163_31472'})
driver.add_cookie({'name': 'BDUSS', 'value': 'hpRVBWSklrMHNjN3lnZGpMM25PM0JCdzZscGR3fnlyZFc3U0FnU2dnYWJCZHRlRVFBQUFBJCQAAAAAAAAAAAEAAACrMBMANTIwc3poAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJt4s16beLNefm'})
driver.get('http://www.baidu.com/')

'''
# inspect
class AAA(object):
    def a(self):
        print 'aa'
        print self.__class__.__name__
        print inspect.stack()[1][3]
        print inspect.stack()
        main_object = inspect.getmembers(inspect.stack()[1][0])[-3][1]['self']
        print str(main_object).split('.')[1].split(' ')[0]
class BBB(object):
    tA = AAA()

    def b_fun(self):
        print 'bb'
        self.tA.a()


if __name__ == '__main__':
    tb = BBB()
    tb.b_fun()
'''



