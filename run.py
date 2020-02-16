# coding=utf-8
# @Time  : 2019/12/22
# @Author: 星空物语
# @File  : run.py
# @Description: 初始化，运行测试，测试收尾

import pytest
import config.config as cf
from util.log import Logger
import argparse
from selenium import webdriver
from util.mail import send_mail


def get_args():
    """命令行参数解析"""
    parser = argparse.ArgumentParser(description=u'可选择参数：')
    parser.add_argument('-e', '--environment', choices=['preview', 'product'], default='preview', help=u'测试环境preview，线上环境product')
    args = parser.parse_args()
    if args.environment in ('pre', 'preview'):
        cf.set_value('environment', 'preview')
        cf.set_value('site', 'http://www.baidu.com/')
    elif args.environment in ('pro', 'product'):
        cf.set_value('environment', 'product')
        cf.set_value('site', 'https://www.baidu.com/')
    else:
        print u"请输入preview/product"
        exit()


def set_driver():
    """设置driver"""
    # 配置Chrome Driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')  # 浏览器最大化
    chrome_options.add_argument('--disable-infobars')  # 不提醒chrome正在受自动化软件控制
    prefs = {'download.default_directory': cf.get_value('download_path')}
    chrome_options.add_experimental_option('prefs', prefs)  # 设置默认下载路径
    # chrome_options.add_argument(r'--user-data-dir=D:\ChromeUserData')  # 设置用户文件夹，可免登陆
    driver = webdriver.Chrome('{}\\driver\\chromedriver.exe'.format(cf.get_value('root_path')), options=chrome_options)
    cf.set_value('driver', driver)


def main():
    """运行pytest命令启动测试"""
    pytest.main(['-v', '-s', 'test_case/', '--html=report/report.html', '--self-contained-html'])


if __name__ == '__main__':
    cf.init()  # 初始化全局变量
    get_args()  # 命令行参数解析
    log = Logger('szh')  # 初始化log配置
    set_driver()  # 初始化driver
    main()  # 运行pytest测试集
    cf.get_value('driver').quit()  # 关闭selenium driver

    # 先将util.mail文件send_mail()中的用户名、密码填写正确，再启用发送邮件功能！！！
    # send_mail(['22459496@qq.com'])  # 将报告发送至邮箱
