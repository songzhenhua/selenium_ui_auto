# coding=utf-8
from page_object.login_page import LoginPage
from page_object.base_page import BasePage
import pytest


class TestLogin():
    """
    pytest:
    测试文件以test_开头
    测试类以Test开头，并且不能带有__init__方法
    测试函数以test_开头
    断言使用assert
    """
    base_page = BasePage()
    login_page = LoginPage(base_page.driver)

    def test_login(self):
        """
        登陆后，判断是否有第一个项目名称，有则登陆成功
        """
        try:
            self.login_page.login()
            self.login_page.wait_element('css,div[class="ng-binding"]')
            assert (u'自动化测试项目' in self.login_page.driver.page_source, 'login failed')
        except Exception, e:
            # print unicode(e.message).encode("utf-8")
            self.login_page.screenshot(u'登陆失败')
            raise e
