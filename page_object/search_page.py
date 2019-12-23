# coding=utf-8
# @Time  : 2019/12/22
# @Author: 星空物语
# @File  : search_page.py
# @Description: 百度搜索页

from page_object.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    # 含_百度百科的搜索结果
    l_baike = 'xpath,//a[(. = "星空物语_百度百科")]'

    # 下一页
    b_next_page = 'xpath,//a[(. = "下一页>")]'

    # 上一页
    b_up_page = 'xpath,//a[(. = "<上一页")]'

    # 点击搜索结果的百科
    def click_result(self):
        self.wait_element(self.l_baike)
        self.open_new_window(self.l_baike)

    # 点击下一页
    def click_next_page(self):
        self.wait_element(self.b_next_page)
        self.click(self.b_next_page)
