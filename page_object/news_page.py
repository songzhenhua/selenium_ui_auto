# coding=utf-8
from page_object.base_page import BasePage


class NewsPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    # 关键字输入框
    i_keyword = 'xpath,//input[@id="ww"]'
    # 百度一下按钮
    b_search = 'xpath,//input[@id="s_btn_wr"]'
    # 轮播图
    d_carousel = 'xpath,//div[@id="imgView"]'

    def open_newspage(self):
        self.open('http://news.baidu.com/')

    # 搜索新闻
    def search(self, keys=u'北京'):
        self.type(self.i_keyword, keys)
        self.click(self.b_search)

    # 点击轮播图
    def click_carousel(self):
        self.click(self.d_carousel)