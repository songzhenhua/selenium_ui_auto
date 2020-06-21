# coding=utf-8
# @Time  : 2020/1/1 17:50
# @Author: zhenhua.song
# @File  : test_news.py
# @Description: 百度新闻页测试用例
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from page_object.news_page import NewsPage
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
    news_page = NewsPage(driver)

    def test_show_QRcode(self):
        """新闻页-显示二维码"""
        try:
            self.news_page.open_newspage()
            self.news_page.move_QRcode()
            assert self.news_page.wait_element(self.news_page.im_QRcode)  # 判断二维码图片出现
            self.news_page.screenshot(u'显示二维码')
        except Exception, e:
            self.news_page.screenshot(u'显示二维码失败')
            raise e

    def test_click_carousel(self):
        """新闻页-点击轮播图"""
        try:
            current_page_num = len(self.driver.window_handles)
            self.news_page.click_carousel()  # 点击轮播图
            assert current_page_num + 1 == len(self.driver.window_handles)  # 判断打开了新的标签页
            self.news_page.close()  # 关闭新打开的页面
        except Exception, e:
            self.news_page.screenshot(u'点击轮播图失败')
            raise e

    def test_search_news(self):
        """新闻页-搜索新闻"""
        try:
            self.news_page.open_newspage()
            self.news_page.search(u'涨工资')  # 搜索涨工资
            assert self.news_page.wait_text(u'电视剧《一起来看流星雨》片头曲')  # 故意断言失败
        except Exception, e:
            self.news_page.screenshot(u'搜索新闻失败')
            raise e


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_search.py'])
    # pytest.main(['-v', '-s'])