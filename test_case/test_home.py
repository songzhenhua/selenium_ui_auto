# coding=utf-8
from page_object.home_page import HomePage
from page_object.base_page import BasePage
from page_object.news_page import NewsPage
from page_object.hao123_page import Hao123Page
from page_object.search_page import SearchPage
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
    news_page = NewsPage(base_page.driver)
    hao123_page = Hao123Page(base_page.driver)
    search_page = SearchPage(base_page.driver)

    # 打开百度首页
    def test_open_homepage(self):
        try:
            self.home_page.open_homepage()
            assert self.home_page.wait_element(self.home_page.l_more_product)  # 是否有‘更多产品’element
            self.home_page.screenshot(u'打开百度首页')
        except Exception, e:
            self.home_page.screenshot(u'打开百度首页失败')
            raise e

    # 输入搜索关键字，自动跳转
    def test_input_keyword(self):
        try:
            self.home_page.open_homepage()
            self.home_page.input_keyword(u'星空物语')  # 输入关键字
            self.search_page.wait_element(self.search_page.l_baike)  # 等待含星空物语_百度百科的搜索结果
            assert self.home_page.text_on_page(u'星空物语_百度百科')  # 输入关键字自动跳搜索结果页，第一项是百科
            self.home_page.screenshot(u'输入关键字跳转')
        except Exception, e:
            self.home_page.screenshot(u'输入关键字跳转失败')
            raise e

    # 打开新闻
    def test_click_news(self):
        try:
            self.home_page.open_homepage()
            self.home_page.click_news()  # 点击新闻
            assert self.home_page.wait_element(self.news_page.d_carousel)  # 轮播图出现
            self.home_page.screenshot(u'打开新闻')
        except Exception, e:
            self.home_page.screenshot(u'打开新闻失败')
            raise e

    # 打开hao123
    def test_click_hao123(self):
        try:
            self.home_page.open_homepage()
            self.home_page.click_hao123()  # 点击hao123
            assert self.home_page.wait_element(self.hao123_page.l_more_product)  # 腾讯链接出现
        except Exception, e:
            self.home_page.screenshot(u'打开hao123失败')
            raise e


if __name__ == '__main__':
    # pytest.main(['-v', '-s', 'test_home.py::TestHome::test_input_keyword'])
    pytest.main(['-v', '-s'])