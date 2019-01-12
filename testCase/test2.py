#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException
from time import sleep


# 试验拖拽

driver = webdriver.Chrome()
driver.get("https://www.helloweba.com/demo/2017/unlock/")
sleep(2)

dragger = driver.find_elements_by_class_name('slide-to-unlock-handle')[0]
actions = ActionChains(driver)
try:
    actions.drag_and_drop_by_offset(dragger, 500, 0).perform()
# 将移动的横坐标设置很大，大于滑动边框的距离，使用drag_and_drop直接移动
except UnexpectedAlertPresentException:
    pass
