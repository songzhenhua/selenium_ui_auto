# coding=utf-8
from page_object.base_page import BasePage


# 百度首页
class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    # 新闻链接
    l_news = 'xpath,//a[@name="tj_trnews"]'
    # hao123链接
    l_hao123 = 'xpath,//a[@name="tj_trhao123"]'
    # 地图链接
    l_map = 'xpath,//a[@name="tj_trmap"]'
    # 视频链接
    l_video = 'xpath,//a[@name="tj_trvideo"]'
    # 贴吧链接
    l_tieba = 'xpath,//a[@name="tj_trtieba"]'
    # 学术链接
    l_xueshu = 'xpath,//a[@name="tj_trxueshu"]'
    # 登陆链接
    l_login = 'xpath,//a[@name="tj_login"]'
    # 设置链接
    l_setting = 'xpath,//a[@name="tj_settingicon"]'
    # 更多产品链接
    l_more_product = 'xpath,//a[@name="tj_briicon"]'
    # 关键字输入框
    i_keyword = 'xpath,//input[ @ id = "kw"]'


    def open_homepage(self):
        self.open('http://www.baidu.com/')

    # 点击新闻
    def click_news(self):
        self.get_element(self.l_news).click()

    # 点击hao123
    def click_hao123(self):
        self.get_element(self.l_hao123).click()

    # 点击地图
    def click_map(self):
        self.get_element(self.l_map).click()

    # 点击视频
    def click_video(self):
        self.get_element(self.l_video).click()

    # 点击学术
    def click_xueshu(self):
        self.get_element(self.l_xueshu).click()

    # 点击贴吧
    def click_tieba(self):
        self.get_element(self.l_tieba).click()

    # 输入搜索关键字
    def input_keyword(self, keys='星空物语'):
        self.type(self.i_keyword, keys)
