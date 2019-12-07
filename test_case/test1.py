#coding=utf-8

from selenium import webdriver
import inspect
import time
import sys
from page_object.home_page import ProjectListPage

# 通过加cookies免登陆
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com/')
time.sleep(60)
driver.add_cookie({'name': 'uid', 'value': '257646cadcf-e748-2a18-5f80a51'})
driver.add_cookie({'name': 'session', 'value': '1bee4b6b272e772c0ecb86bc6969a3d5e2b1e22ca9d'})
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



