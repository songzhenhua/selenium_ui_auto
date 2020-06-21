# coding=utf-8
# @Time  : 2019/12/22
# @Author: 星空物语
# @File  : base_page.py
# @Description: 每个PO文件的父类，二次封装selenium常用操作，提供上层操作

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
import inspect
import config.config as cf
import logging
import time

log = logging.getLogger('szh.BasePage')


class BasePage(object):
    def __init__(self):
        self.driver = cf.get_value('driver')  # 从全局变量取driver

    def split_locator(self, locator):
        """
        分解定位表达式，如'css,.username',拆分后返回'css selector'和定位表达式'.username'(class为username的元素)
        :param locator: 定位方法+定位表达式组合字符串，如'css,.username'
        :return: locator_dict[by], value:返回定位方式和定位表达式
        """
        by = locator.split(',', 1)[0]
        value = locator.split(',', 1)[1]
        locator_dict = {
            'id': 'id',
            'name': 'name',
            'class': 'class name',
            'tag': 'tag name',
            'link': 'link text',
            'plink': 'partial link text',
            'xpath': 'xpath',
            'css': 'css selector',
        }
        if by not in locator_dict.keys():
            raise NameError("wrong locator!'id','name','class','tag','link','plink','xpath','css',exp:'id,username'")
        return locator_dict[by], value

    def wait_element(self, locator, sec=30):
        """
        等待元素出现
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :param sec:等待秒数
        """
        by, value = self.split_locator(locator)
        try:
            WebDriverWait(self.driver, sec, 1).until(lambda x: x.find_element(by=by, value=value),
                                                     message='element not found!!!')
            log.info(u'等待元素：%s' % locator)
            return True
        except TimeoutException:
            return False
        except Exception, e:
            raise e

    def get_element(self, locator, sec=60):
        """
        获取一个元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :param sec:等待秒数
        :return: 元素可找到返回element对象，否则返回False
        """
        if self.wait_element(locator, sec):
            by, value = self.split_locator(locator)
            try:
                element = self.driver.find_element(by=by, value=value)
                log.info(u'获取元素：%s' % locator)
                return element
            except Exception, e:
                raise e
        else:
            return False

    def get_elements(self, locator):
        """
        获取一组元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :return: elements
        """
        by, value = self.split_locator(locator)
        try:
            elements = WebDriverWait(self.driver, 60, 1).until(lambda x: x.find_elements(by=by, value=value))
            log.info(u'获取元素列表：%s' % locator)
            return elements
        except Exception, e:
            raise e

    def get_url(self):
        """
        获取当前网址
        :return: 网址连接
        """
        log.info(u'获取当前网址：%s' % self.driver.current_url)
        return self.driver.current_url

    def open(self, url):
        """
        打开网址
        :param url: 网址连接
        """
        self.driver.get(url)
        log.info(u'打开网址：%s' % url)

    def clear(self, locator):
        """
        清除元素中的内容
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        """
        self.get_element(locator).clear()
        log.info(u'清空内容：%s' % locator)

    def type(self, locator, text):
        """
        在元素中输入内容
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :param text: 输入的内容
        """
        self.get_element(locator).send_keys(text)
        log.info(u'向元素 %s 输入文字：%s' % (locator, text))

    def type_all(self, locator, text):
        """
        在符合条件的所有元素中输入内容，依次循环输入text1,text2……
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :param text: 输入的内容
        """
        allt = self.get_elements(locator)
        i = 1
        log.info(u'开始执行type_all，共%s个元素' % (len(allt)))
        for ele in allt:
            newtext = text + str(i)
            ele.send_keys(newtext)
            log.info(u'向第 %s 个元素输入文字：%s' % (i, newtext))
            i += 1

    def enter(self, locator):
        """
        在元素上按回车键
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        """
        self.get_element(locator).send_keys(Keys.ENTER)
        log.info(u'在元素 %s 上按回车' % locator)

    def click(self, locator, repeat=0):
        """
        在元素上单击
        :param repeat: 重复次数标记，不要填写
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        """
        try:
            repeat += 1
            self.get_element(locator).click()
            log.info(u'点击元素：%s' % locator)
        except Exception, e:
            log.info(u'点击元素：%s 第%s次执行失败' % (locator, repeat))
            if repeat > 2:
                raise e
            self.click(locator, repeat)

    def click_all(self, locator):
        """
        点击所有符合条件的元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        """
        allc = self.get_elements(locator)
        i = 0
        log.info(u'开始执行click_all，共%s个元素' % (len(allc)))
        for ele in allc:
            self.sleep(0.3)
            ele.click()
            i += 1
            log.info(u'点击第 %s 个元素' % i)

    def double_click_all(self, locator):
        """
        双击所有符合条件的元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        """
        allc = self.get_elements(locator)
        i = 0
        log.info(u'开始执行double_click_all，共%s个元素' % (len(allc)))
        for ele in allc:
            ActionChains(self.driver).double_click(ele).perform()
            i += 1
            log.info(u'点击第 %s 个元素' % i)

    def get_element_offset(self, locator):
        """
        获取元素坐标
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :return: x,y
        """
        element = self.get_element(locator)
        loc = element.location
        x = loc['x']
        y = loc['y']
        log.info(u'获取元素坐标：%s,%s' % (x, y))
        return x, y

    def get_element_offset_click(self, locator):
        """
        获取元素坐标并点击中间位置，适用于：元素A中套着元素B，元素B无法定位但元素A可以定位
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        """
        element = self.get_element(locator)
        loc = element.location
        x = loc['x']
        y = loc['y']
        size = element.size
        width = size['width']
        height = size['height']
        x += width
        y += height
        self.click_offset(x, y)

    def click_offset(self, x, y):
        """
        点击坐标
        :param x: x坐标'
        :param y: y坐标'

        """
        ActionChains(self.driver).move_by_offset(x, y).click().perform()
        log.info(u'点击坐标%s,%s' % (x, y))

    def right_click(self, locator):
        """
        鼠标右击元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        """
        element = self.get_element(locator)
        ActionChains(self.driver).context_click(element).perform()
        log.info(u'在元素上右击：%s' % locator)

    def double_click(self, locator):
        """
        双击元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        """
        element = self.get_element(locator)
        ActionChains(self.driver).double_click(element).perform()
        log.info(u'在元素上双击：%s' % locator)

    def move_to_element(self, locator):
        """
        鼠标指向元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        """
        element = self.get_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()
        log.info(u'指向元素%s' % locator)

    def drag_and_drop(self, locator, target_locator):
        """
        拖动一个元素到另一个元素位置
        :param locator: 要拖动元素的定位
        :param target_locator: 目标位置元素的定位
        """
        element = self.get_element(locator)
        target_element = self.get_element(target_locator)
        ActionChains(self.driver).drag_and_drop(element, target_element).perform()
        log.info(u'把元素 %s 拖至元素 %s' % (locator, target_locator))

    def drag_and_drop_by_offset(self, locator, xoffset, yoffset):
        """
        拖动一个元素移动x,y个偏移量
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :param xoffset: X offset to move to
        :param yoffset: Y offset to move to
        """
        element = self.get_element(locator)
        ActionChains(self.driver).drag_and_drop_by_offset(element, xoffset, yoffset).perform()
        log.info(u'把元素 %s 拖至坐标：%s %s' % (locator, xoffset, yoffset))

    def click_partial_text_link(self, text):
        """
        按部分链接文字查找并点击链接
        :param text: 链接的部分文字
        """
        self.get_element('plink,' + text).click()
        log.info(u'点击连接：%s' % text)

    def alert_text(self):
        """
        返回alert文本
        :return: alert文本
        """
        log.info(u'获取弹框文本：%s' % self.driver.switch_to.alert.text)
        return self.driver.switch_to.alert.text

    def alert_accept(self):
        """
        alert点确认
        """
        self.driver.switch_to.alert.accept()
        log.info(u'点击弹框确认')

    def alert_dismiss(self):
        """
        alert点取消
        """
        self.driver.switch_to.alert.dismiss()
        log.info(u'点击弹框取消')

    def get_attribute(self, locator, attribute):
        """
        返回元素某属性的值
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :param attribute: 属性名称
        :return: 属性值
        """
        value = self.get_element(locator).get_attribute(attribute)
        log.info(u'获取元素 %s 的属性值 %s 为：%s' % (locator, attribute, value))
        return value

    def get_ele_text(self, locator):
        """
        返回元素的文本
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :return: 元素的文本
        """
        log.info(u'获取元素 %s 的文本为：%s' % (locator, self.get_element(locator).text))
        return self.get_element(locator).text

    def frame_in(self, locator):
        """
        进入frame
        :param locator: 定位方法+定位表达式组合字符串，如'css,.username'
        """
        e = self.get_element(locator)
        self.driver.switch_to.frame(e)
        log.info(u'进入frame：%s' % locator)

    def frame_out(self):
        """
        退出frame返回默认文档
        """
        self.driver.switch_to.default_content()
        log.info(u'退出frame返回默认文档')

    def open_new_window_by_locator(self, locator):
        """
        点击元素打开新窗口，并将句柄切换到新窗口
        :param locator: 定位方法+定位表达式组合字符串，如'css,.username'
        """
        self.get_element(locator).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        log.info(u'点击元素 %s 打开新窗口' % locator)

        # old_handle = self.driver.current_window_handle
        # self.get_element(locator).click()
        # all_handles = self.driver.window_handles
        # for handle in all_handles:
        #     if handle != old_handle:
        #         self.driver.switch_to.window(handle)

    def open_new_window_by_element(self, element):
        """
        点击元素打开新窗口，并将句柄切换到新窗口
        :param element: 元素对象
        """
        element.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        log.info(u'点击元素打开新窗口')

    def js(self, script):
        """
        执行JavaScript
        :param script:js语句 
        """
        self.driver.execute_script(script)
        log.info(u'执行JS语句：%s' % script)

    def scroll_element(self, locator):
        """
        拖动滚动条至目标元素
        :param locator: 定位方法+定位表达式组合字符串，如'css,.username'
        """
        script = "return arguments[0].scrollIntoView();"
        element = self.get_element(locator)
        self.driver.execute_script(script, element)
        log.info(u'滚动至元素：%s' % locator)

    def scroll_top(self):
        """
        滚动至顶部
        """
        self.js("window.scrollTo(document.body.scrollHeight,0)")
        log.info(u'滚动至顶部')

    def scroll_bottom(self):
        """
        滚动至底部
        """
        self.js("window.scrollTo(0,document.body.scrollHeight)")
        log.info(u'滚动至底部')

    def back(self):
        """
        页面后退
        """
        self.driver.back()
        log.info(u'页面后退')

    def forward(self):
        """
        页面向前
        """
        self.driver.forward()
        log.info(u'页面向前')

    def wait_text(self, text, per=3, count=10):
        """
        判断给定文本是否在页面上
        :param text: 要判断的文本
        :param per: 每次判断间断时间
        :param count: 判断次数
        :return: 存在返回True，不存在返回False
        """
        for i in range(count):
            if text in self.driver.page_source:
                log.info(u'判断页面上有文本：%s 第%s次' % (text, i+1))
                return True
            self.sleep(per)
        log.info(u'判断页面上没有文本：%s 共%s次' % (text, i+1))
        return False

    def refresh(self):
        """
        刷新页面
        """
        self.driver.refresh()
        log.info(u'刷新页面')

    def screenshot(self, info='-'):
        """
        截图,起名为：文件名-方法名-注释
        :param info: 截图说明
        """
        catalog_name = cf.get_value('screenshot_path')  # 从全局变量取截图文件夹位置
        if not os.path.exists(catalog_name):
            os.makedirs(catalog_name)
        class_object = inspect.getmembers(inspect.stack()[1][0])[-3][1]['self']  # 获得测试类的object
        classname = str(class_object).split('.')[1].split(' ')[0]  # 获得测试类名称
        testcase_name = inspect.stack()[1][3]  # 获得测试方法名称
        filepath = catalog_name + classname + "@" + testcase_name + info + ".png"
        self.driver.get_screenshot_as_file(filepath)
        log.info(u'截图：%s.png' % info)

    def close(self):
        """
        关闭当前页
        """
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        log.info(u'关闭当前Tab')

    def sleep(self, sec):
        time.sleep(sec)
        log.info(u'等待%s秒' % sec)


if __name__ == '__main__':
    bp = BasePage()
    bp.open('http://www.baidu.com')
