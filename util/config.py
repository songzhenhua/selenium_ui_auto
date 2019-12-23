# coding=utf-8
# @Time  : 2019/12/22
# @Author: 星空物语
# @File  : config.py
# @Description: 存放全局变量，并提供存、取方法

from selenium import webdriver


def init():
    global _global_dict
    _global_dict = {}

    # 配置Chrome Driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')  # 浏览器最大化
    chrome_options.add_argument('--disable-infobars')  # 不提醒chrome正在受自动化软件控制
    prefs = {'download.default_directory': 'd:\\'}
    chrome_options.add_experimental_option('prefs', prefs)  # 设置默认下载路径
    # chrome_options.add_argument(r'--user-data-dir=D:\ChromeUserData')  # 设置用户文件夹，可免登陆
    driver = webdriver.Chrome('D:\\code\\python\\selenium_ui_auto\\driver\\'+'chromedriver.exe', options=chrome_options)

    _global_dict['driver'] = driver
    _global_dict['screenshot_path'] = "D:\\code\\python\\selenium_ui_auto\\file\\screenshot\\"  # 存放正常截图文件夹
    _global_dict['errorshot_path'] = "D:\\code\\python\\selenium_ui_auto\\file\\errorshot\\"  # 存放报错时截图文件夹


def set_value(name, value):
    _global_dict[name] = value


def get_value(name, def_val='no_value'):
    try:
        return _global_dict[name]
    except KeyError:
        return def_val
