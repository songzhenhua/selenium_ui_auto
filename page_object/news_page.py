# coding=utf-8
# @Time  : 2019/12/22
# @Author: 星空物语
# @File  : news_page.py
# @Description: 百度新闻页

from page_object.base_page import BasePage
import config.config as cf


class NewsPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    # i=输入框, l=链接, im=图片, t=文字控件, d=div, lab=label
    # 关键字输入框
    i_keyword = 'xpath,//input[@id="ww"]'
    # 百度一下按钮
    b_search = 'xpath,//input[@id="s_btn_wr"]'
    # 轮播图
    d_carousel = 'xpath,//div[@id="imgView"]'
    # 二维码图标
    icon_QRcode = 'xpath,//li[@class="item qr-code button-rotate"]'
    # 二维码图片
    im_QRcode = 'xpath,//li[@class="qr-code-container clearfix"]/span/span/img'
    # 搜索结果第一个标题
    l_result1 = 'xpath,//h3[@class="c-title"]'

    def open_newspage(self):
        site = cf.get_value('site').replace('www', 'news')  # 从全局变量取百度地址并替换为新闻地址
        self.open(site)

    # 搜索新闻
    def search(self, keys=u'北京'):
        self.type(self.i_keyword, keys)
        self.click(self.b_search)

    # 点击轮播图
    def click_carousel(self):
        self.open_new_window_by_locator(self.d_carousel)

    # 指向二维码
    def move_QRcode(self):
        self.move_to_element(self.icon_QRcode)