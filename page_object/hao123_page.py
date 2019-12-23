# coding=utf-8
# @Time  : 2019/12/22
# @Author: 星空物语
# @File  : hao123_page.py
# @Description: hao123页面

from page_object.base_page import BasePage


class Hao123Page(BasePage):
    def __init__(self, driver):
        self.driver = driver

    # 腾讯链接
    l_more_product = 'xpath,//a[@data-title="腾讯"]'

    def open_hao123page(self):
        self.open('https://www.hao123.com/')

    # 点击腾讯链接
    def click_tx(self):
        self.click(self.l_more_product)

