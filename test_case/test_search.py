# coding=utf-8
# @Time  : 2019/12/22
# @Author: 星空物语
# @File  : config.py
# @Description: 百度搜索页测试用例
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from page_object.home_page import HomePage
from page_object.search_page import SearchPage
import pytest
import config.config as cf


class TestSearch():
    """
    pytest:
    测试文件以test_开头
    测试类以Test开头，并且不能带有__init__方法
    测试函数以test_开头
    断言使用assert
    """
    driver = cf.get_value('driver')  # 从全局变量取driver
    home_page = HomePage(driver)
    search_page = SearchPage(driver)

    def test_click_result(self):
        """搜索页-点击首个搜索结果"""
        try:
            self.home_page.open_homepage()
            self.home_page.input_keyword(u'星空物语')  # 输入关键字
            self.search_page.click_result()  # 点击百科
            assert self.home_page.wait_text(u'电视剧《一起来看流星雨》片头曲')  # 验证页面打开
            self.home_page.screenshot(u'打开搜索结果')
            self.search_page.close()  # 关闭百科页面
        except Exception, e:
            self.home_page.screenshot(u'打开搜索结果失败')
            raise e

    def test_click_next_page(self):
        """搜索页-搜索翻页"""
        try:
            self.search_page.click_next_page()  # 点下一页
            assert self.home_page.wait_element(self.search_page.b_up_page)  # 上一页出现
            self.search_page.scroll_element(self.search_page.b_up_page)  # 滚到上一页
            self.home_page.screenshot(u'搜索翻页')
        except Exception, e:
            self.home_page.screenshot(u'搜索翻页失败')
            raise e


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_search.py'])
    # pytest.main(['-v', '-s'])