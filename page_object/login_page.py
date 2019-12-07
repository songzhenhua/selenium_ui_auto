# coding=utf-8
from page_object.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.open('http://www.baidu.com/')

