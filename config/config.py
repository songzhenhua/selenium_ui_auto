# coding=utf-8
# @Time  : 2019/12/22
# @Author: 星空物语
# @File  : config.py
# @Description: 存放全局变量，并提供存、取方法

import os


def init():
    global _global_dict
    _global_dict = {}

    # 代码根目录
    root_dir = os.getcwd()

    # 存放程序所在目录
    _global_dict['root_path'] = root_dir
    # 存放正常截图文件夹
    _global_dict['screenshot_path'] = "{}\\file\\screenshot\\".format(root_dir)
    # 下载文件夹
    _global_dict['download_path'] = "{}\\file\\download\\".format(root_dir)
    # 上传文件夹
    _global_dict['upload_path'] = "{}\\file\\upload\\".format(root_dir)
    # 存放报告路径
    _global_dict['report_path'] = "{}\\report\\".format(root_dir)

    # 保存driver
    _global_dict['driver'] = None

    # 设置运行环境网址主页
    _global_dict['site'] = 'https://www.baidu.com/'
    # 运行环境，默认preview，可设为product
    _global_dict['environment'] = 'preview'


def set_value(name, value):
    """
    修改全局变量的值
    :param name: 变量名
    :param value: 变量值
    """
    _global_dict[name] = value


def get_value(name, def_val='no_value'):
    """
    获取全局变量的值
    :param name: 变量名
    :param def_val: 默认变量值
    :return: 变量存在时返回其值，否则返回'no_value'
    """
    try:
        return _global_dict[name]
    except KeyError:
        return def_val


if __name__ == '__main__':
    init()