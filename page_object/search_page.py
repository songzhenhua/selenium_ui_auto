# coding=utf-8
# @Time  : 2019/12/22
# @Author: 星空物语
# @File  : search_page.py
# @Description: 百度搜索页

from page_object.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    # i=输入框, l=链接, im=图片, t=文字控件, d=div, lab=label
    # 含_百度百科的搜索结果
    l_baike = 'xpath,//a[(. = "星空物语_百度百科")]'

    # 下一页
    b_next_page = 'link,下一页>'

    # 上一页
    b_up_page = 'xpath,//a[(. = "<上一页")]'

    # 点击搜索结果的百科
    def click_result(self):
        self.open_new_window_by_locator(self.l_baike)
        self.sleep(3)

    # 点击下一页
    def click_next_page(self):
        self.click(self.b_next_page)
