# coding=utf-8
from page_object.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.open('http://www.baidu.com/')

