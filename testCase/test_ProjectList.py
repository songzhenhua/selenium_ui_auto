# coding=utf-8
from pageObject.LoginPage import LoginPage
from pageObject.ProjectListPage import ProjectListPage
from pageObject.BasePage import BasePage
import unittest


class TestProjectList(unittest.TestCase):
    base_page = BasePage()
    login_page = LoginPage(base_page.driver)
    projectList_page = ProjectListPage(base_page.driver)
    login_page.login()

    @classmethod
    def tearDownClass(cls):
        cls.base_page.driver.quit()

    # 点击一个项目
    def test1_click_project(self):
        try:
            self.projectList_page.click_project()
            self.assertTrue(self.projectList_page.wait_element('plink,数据'), u'打开项目失败')
        except Exception, e:
            self.projectList_page.screenshot(u'打开项目失败')
            raise e
        finally:
            self.projectList_page.close()

    # 点击‘新建项目’按钮
    def test2_click_create(self):
        try:
            self.projectList_page.click_create()
            # 断言上部的步骤名称元素
            self.assertTrue(self.projectList_page.wait_element('css,div.step-desc.ng-binding'), u'打开新建项目页失败')
        except Exception, e:
            self.projectList_page.screenshot(u'打开新建项目页失败')
            raise e
        finally:
            self.projectList_page.close()

    # 点击消息中心
    def test3_click_message(self):
        try:
            self.projectList_page.click_message()
            self.assertTrue(self.projectList_page.wait_element('plink,收件箱'), u'打开消息中心失败')
        except Exception, e:
            self.projectList_page.screenshot(u'打开消息中心失败')
            raise e

    # 点击记录
    def test4_click_record(self):
        try:
            self.projectList_page.click_record()
            self.assertTrue(self.projectList_page.wait_element('plink,记录'), u'打开记录失败')
        except Exception, e:
            self.projectList_page.screenshot(u'打开记录失败')
            raise e

    # 退出登录
    def test5_click_exit(self):
        try:
            self.projectList_page.logout()
            self.assertTrue(self.projectList_page.wait_element('css,input[placeholder="用户名"]'), u'退出失败')
        except Exception, e:
            self.projectList_page.screenshot(u'退出失败')
            raise e
