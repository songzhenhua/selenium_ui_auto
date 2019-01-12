# coding=utf-8
from pageObject.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.open('http://www.xxx.cn/')
        self.get_element('css,input[placeholder="用户名"]').send_keys('songzhenhua')  # 输入用户名
        self.get_element('css,input[placeholder="密码"]').send_keys('123456')  # 输入密码
        self.get_element('css,button[type="button"]').click()  # 点击登陆按钮
        self.wait_element('css,#name')

