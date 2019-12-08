# coding=utf-8
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

