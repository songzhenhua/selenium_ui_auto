# coding=utf-8
from page_object.home_page import HomePage
from page_object.base_page import BasePage
import pytest


class TestHome():
    """
    pytest:
    测试文件以test_开头
    测试类以Test开头，并且不能带有__init__方法
    测试函数以test_开头
    断言使用assert
    """
    base_page = BasePage()
    home_page = HomePage(base_page.driver)

    # 打开百度首页
    def test_open_homepage(self):
        try:
            self.home_page.open_homepage()
            assert self.home_page.wait_element(self.home_page.l_more_product)
        except Exception, e:
            self.home_page.screenshot(u'打开百度首页失败')
            raise e

    # 输入搜索关键字
    def test_input_keyword(self):
        try:
            self.home_page.open_homepage()
            self.home_page.input_keyword('星空物语')
            assert 1  # self.home_page.wait_element(self.home_page.link_more_product)
        except Exception, e:
            self.home_page.screenshot(u'打开新闻失败')
            raise e

    # 打开新闻
    def test_click_news(self):
        try:
            self.home_page.open_homepage()
            self.home_page.click_news()
            assert 1  # self.home_page.wait_element(self.home_page.link_more_product)
        except Exception, e:
            self.home_page.screenshot(u'打开新闻失败')
            raise e

    # 打开hao123
    def test_click_hao123(self):
        try:
            self.home_page.open_homepage()
            self.home_page.click_hao123()
            assert 1  # self.home_page.wait_element(self.home_page.link_more_product)
        except Exception, e:
            self.home_page.screenshot(u'打开hao123失败')
            raise e

    # 打开地图
    def test_click_map(self):
        try:
            self.home_page.open_homepage()
            self.home_page.click_map()
            assert 1  # self.home_page.wait_element(self.home_page.link_more_product)
        except Exception, e:
            self.home_page.screenshot(u'打开click_map失败')
            raise e

    # 打开视频
    def test_click_video(self):
        try:
            self.home_page.open_homepage()
            self.home_page.click_video()
            assert 1  # self.home_page.wait_element(self.home_page.link_more_product)
        except Exception, e:
            self.home_page.screenshot(u'打开视频失败')
            raise e

    # 打开学术
    def test_click_xueshu(self):
        try:
            self.home_page.open_homepage()
            self.home_page.click_xueshu()
            assert 1  # self.home_page.wait_element(self.home_page.link_more_product)
        except Exception, e:
            self.home_page.screenshot(u'打开学术失败')
            raise e

    # 打开贴吧
    def test_click_tieba(self):
        try:
            self.home_page.open_homepage()
            self.home_page.click_tieba()
            assert 1  # self.home_page.wait_element(self.home_page.link_more_product)
        except Exception, e:
            self.home_page.screenshot(u'打开贴吧失败')
            raise e