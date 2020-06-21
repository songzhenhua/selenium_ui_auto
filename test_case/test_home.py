# coding=utf-8
# @Time  : 2019/12/22
# @Author: 星空物语
# @File  : config.py
# @Description: 百度首页测试用例
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from page_object.home_page import HomePage
from page_object.news_page import NewsPage
from page_object.hao123_page import Hao123Page
from page_object.search_page import SearchPage
import pytest
import config.config as cf
import logging


log = logging.getLogger('szh.TestHome')


class TestHome():
    """
    pytest:
    测试文件以test_开头
    测试类以Test开头，并且不能带有__init__方法
    测试函数以test_开头
    断言使用assert
    """

    driver = cf.get_value('driver')  # 从全局变量取driver
    home_page = HomePage(driver)
    news_page = NewsPage(driver)
    hao123_page = Hao123Page(driver)
    search_page = SearchPage(driver)

    def test_open_homepage(self):
        """首页-打开百度首页"""
        try:
            self.home_page.open_homepage()
            assert self.home_page.wait_element(self.home_page.l_more_product)  # 有‘更多产品’element
            log.info(u'断言有‘更多产品’元素 成功')
            self.home_page.screenshot(u'打开百度首页')
        except Exception, e:
            self.home_page.screenshot(u'打开百度首页失败')
            raise e

    def test_input_keyword(self):
        """首页-输入搜索关键字，自动跳转"""
        try:
            self.home_page.open_homepage()
            self.home_page.input_keyword(u'星空物语')  # 输入关键字
            self.search_page.wait_element(self.search_page.l_baike)  # 等待含星空物语_百度百科的搜索结果
            assert self.home_page.wait_text(u'星空物语_百度百科')  # 输入关键字自动跳搜索结果页，第一项是百科
            log.info(u'断言有‘星空物语_百度百科’文字 成功')
            self.home_page.screenshot(u'输入关键字跳转')
        except Exception, e:
            self.home_page.screenshot(u'输入关键字跳转失败')
            raise e

    def test_click_news(self):
        """首页-打开新闻"""
        try:
            self.home_page.open_homepage()
            self.home_page.click_news()  # 点击新闻
            assert self.home_page.wait_element(self.news_page.d_carousel)  # 轮播图出现
            log.info(u'断言有‘轮播图’元素 成功')
            self.home_page.screenshot(u'打开新闻')
        except Exception, e:
            self.home_page.screenshot(u'打开新闻失败')
            raise e

    def test_click_hao123(self):
        """首页-打开hao123"""
        try:
            self.home_page.open_homepage()
            self.home_page.click_hao123()  # 点击hao123
            assert self.home_page.wait_element(self.hao123_page.l_more_product)  # 腾讯链接出现
            log.info(u'断言有‘腾讯链接’ 成功')
        except Exception, e:
            self.home_page.screenshot(u'打开hao123失败')
            raise e


if __name__ == '__main__':
    # pytest.main(['-v', '-s', 'test_home.py::TestHome::test_input_keyword'])
    pytest.main(['-v', '-s'])