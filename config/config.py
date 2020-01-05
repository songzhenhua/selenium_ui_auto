# coding=utf-8
# @Time  : 2019/12/22
# @Author: 星空物语
# @File  : config.py
# @Description: 存放全局变量，并提供存、取方法

from selenium import webdriver
import os


def init():
    global _global_dict
    _global_dict = {}

    # 代码根目录
    root_dir = os.getcwd()

    # 存放正常截图文件夹
    _global_dict['screenshot_path'] = "{}\\file\\screenshot\\".format(root_dir)
    # 存放报错时截图文件夹
    _global_dict['errorshot_path'] = "{}\\file\\errorshot\\".format(root_dir)
    # 下载文件夹
    _global_dict['download_path'] = "{}\\file\\download\\".format(root_dir)
    # 上传文件夹
    _global_dict['upload_path'] = "{}\\file\\upload\\".format(root_dir)

    # 配置Chrome Driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')  # 浏览器最大化
    chrome_options.add_argument('--disable-infobars')  # 不提醒chrome正在受自动化软件控制
    prefs = {'download.default_directory': _global_dict['download_path']}
    chrome_options.add_experimental_option('prefs', prefs)  # 设置默认下载路径
    # chrome_options.add_argument(r'--user-data-dir=D:\ChromeUserData')  # 设置用户文件夹，可免登陆
    print '{}\\driver\\chromedriver.exe'.format(root_dir)
    driver = webdriver.Chrome('{}\\driver\\chromedriver.exe'.format(root_dir), options=chrome_options)

    # 保存driver
    _global_dict['driver'] = driver


def set_value(name, value):
    _global_dict[name] = value


def get_value(name, def_val='no_value'):
    try:
        return _global_dict[name]
    except KeyError:
        return def_val


if __name__ == '__main__':
    init()