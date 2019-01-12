# coding=utf-8
from pageObject.LoginPage import LoginPage
from pageObject.BasePage import BasePage
import unittest


class TestLogin(unittest.TestCase):
    base_page = BasePage()
    login_page = LoginPage(base_page.driver)

    @classmethod
    def tearDownClass(cls):
        cls.login_page.driver.quit()

    def test_login(self):
        """
        登陆后，判断是否有第一个项目名称，有则登陆成功
        """
        try:
            self.login_page.login()
            self.login_page.wait_element('css,div[class="ng-binding"]')
            self.assertTrue(u'自动化测试项目' in self.login_page.driver.page_source, 'login failed')
        except Exception, e:
            # print unicode(e.message).encode("utf-8")
            self.login_page.screenshot(u'登陆失败')
            raise e
