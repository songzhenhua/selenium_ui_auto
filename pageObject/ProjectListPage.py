# coding=utf-8
from pageObject.BasePage import BasePage


# 登陆后的项目列表页
class ProjectListPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    # 点击项目名称
    def click_project(self):
        project_names = self.get_elements('css,span[ng-bind="c.name"]')  # 项目名称list
        for element in project_names:
            if element.text == u'自动化测试项目':
                self.open_new_window_by_element(element)
                break
        self.sleep(3)
        # 关闭首次进入项目的弹窗
        # self.get_element('css,.fpm-close').click()

    # 点击新建项目按钮
    def click_create(self):
        self.open_new_window('plink,新建项目')

    # 点击右上姓名
    def click_username(self):
        self.get_element('css,span[class="fpm-menu-button-label ng-binding"]').click()

    # 点击消息中心
    def click_message(self):
        self.click_username()
        self.get_element('plink,消息中心').click()

    # 点击记录
    def click_record(self):
        self.click_username()
        self.get_element('plink,记录').click()

    # 退出登录
    def logout(self):
        self.get_element('css,div.ivu-menu-submenu-title').click()  # 右上姓名元素换了，重新定位
        self.sleep(1)
        self.get_element('xpath,//li[text()="退出登录"]').click()

