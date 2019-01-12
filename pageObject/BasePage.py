# coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import inspect


class BasePage(object):
    def __init__(self, browser='chrome'):
        """
        初始化selenium webdriver，默认为chromedriver
        :param browser: chrome,firefox/ff
        """
        browser = browser.lower()
        if browser == 'firefox' or browser == 'ff':
            driver = webdriver.Firefox()
        else:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--start-maximized')  # 浏览器最大化
            chrome_options.add_argument('--disable-infobars')  # 不提醒chrome正在受自动化软件控制
            # chrome_options.add_argument(r'--user-data-dir=D:\ChromeUserData')  # 设置用户文件夹，可免登陆
            driver = webdriver.Chrome(chrome_options=chrome_options)
        try:
            self.driver = driver
        except Exception, e:
            raise e

    def split_locator(self, locator):
        """
        分解定位表达式，如'css,.username',拆分后返回'css selector'和定位表达式'.username'(class为username的元素)
        :param locator: 定位方法+定位表达式组合字符串，如'css,.username'
        :return: locator_dict[by], value:返回定位方式和定位表达式
        """
        by = locator.split(',')[0]
        value = locator.split(',')[1]
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
            WebDriverWait(self.driver, sec, 1).until(lambda x: x.find_element(by=by, value=value))
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
            return elements
        except Exception, e:
            raise e

    def open(self, url):
        """
        打开网址
        :param url: 网址连接
        """
        self.driver.get(url)

    def clear(self, element):
        """
        清除元素中的内容
        :param element: 元素对象
        """
        element.clear()

    def type(self, element, text):
        """
        在元素中输入内容
        :param element: 元素对象
        :param text: 输入的内容
        """
        element.send_keys(text)

    def enter(self, element):
        """
        在元素上按回车键
        :param element: 元素对象
        """
        element.send_keys(Keys.ENTER)

    def click(self, element):
        """
        在元素上单击
        :param element: 元素对象
        """
        element.click()

    def move_to_element(self, element):
        """
        鼠标指向元素
        :param element: 元素对象
        """
        ActionChains(self.driver).move_to_element(element).perform()

    def double_click(self, element):
        """
        双击元素
        :param element: 元素对象
        """
        ActionChains(self.driver).double_click(element).perform()

    def drag_and_drop(self, element, target_element):
        """
        拖动一个元素到另一个元素位置
        :param element: 要拖动的元素
        :param target_element: 目标位置元素
        """
        ActionChains(self.driver).drag_and_drop(element, target_element).perform()

    def drag_and_drop_by_offset(self, element, xoffset, yoffset):
        """
        拖动一个元素向右下移动x,y个偏移量
        :param element: 要拖动的元素
        :param xoffset: X offset to move to
        :param yoffset: Y offset to move to
        """
        ActionChains(self.driver).drag_and_drop_by_offset(element, xoffset, yoffset).perform()

    def click_link(self, text):
        """
        按部分链接文字查找并点击链接
        :param text: 链接的部分文字
        """
        self.get_element('plink,'+text).click()

    def alert_text(self):
        """
        返回alert文本
        :return: alert文本
        """
        return self.driver.switch_to.alert.text

    def alert_accept(self):
        """
        alert点确认
        """
        self.driver.switch_to.alert.accept()

    def alert_dismiss(self):
        """
        alert点取消
        """
        self.driver.switch_to.alert.dismiss()

    def get_attribute(self, element, attribute):
        """
        返回元素某属性的值
        :param element: 元素对象
        :param attribute: 属性名称
        :return: 属性值
        """
        return element.get_attribute(attribute)

    def get_text(self, element):
        """
        返回元素的文本
        :param element: 元素对象
        :return: 元素的文本
        """
        return element.text

    def frame_in(self, locator):
        """
        进入frame
        :param locator: 定位方法+定位表达式组合字符串，如'css,.username'
        """
        e = self.get_element(locator)
        self.driver.switch_to.frame(e)

    def frame_out(self):
        """
        返回主文档
        """
        self.driver.switch_to.default_content()

    def open_new_window(self, locator):
        """
        点击元素打开新窗口，并将句柄切换到新窗口
        :param locator: 定位方法+定位表达式组合字符串，如'css,.username'
        """
        self.get_element(locator).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
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

    def js(self, script):
        """
        执行JavaScript
        :param script:js语句 
        """
        self.driver.execute_script(script)

    def back(self):
        """
        页面后退
        """
        self.driver.back()

    def forward(self):
        """
        页面向前
        """
        self.driver.forward()

    def page_source(self):
        """
        返回页面源代码
        :return: 页面源代码
        """
        return self.driver.page_source

    def f5(self):
        """
        刷新页面
        """
        self.driver.refresh()

    def screenshot(self, info='-'):
        """
        截图
        :param info: 截图说明
        """
        catalog_name = "D:\\"
        class_object = inspect.getmembers(inspect.stack()[1][0])[-3][1]['self']  # 获得测试类的object
        classname = str(class_object).split('.')[1].split(' ')[0]  # 测试类名称
        testcase_name = inspect.stack()[1][3]  # 测试方法名称
        filepath = catalog_name + classname + "-" + testcase_name + info + ".png"
        self.driver.get_screenshot_as_file(filepath)

    def close(self):
        """
        关闭当前页
        """
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def sleep(self, sec):
        time.sleep(sec)

if __name__ == '__main__':
    bp = BasePage()
    # bp.sleep(5)
    bp.open('http://www.baidu.com')