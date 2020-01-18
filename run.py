# coding=utf-8
# @Time  : 2019/12/22
# @Author: 星空物语
# @File  : run.py
# @Description: 初始化，运行测试，测试收尾

import pytest
import config.config as cf
from util.log import Logger


def main():
    pytest.main(['-v', '-s', 'test_case/test_search.py', '--html=report/report.html', '--self-contained-html'])


if __name__ == '__main__':
    cf.init()  # 初始化全局变量
    log = Logger('szh')
    main()  # 运行pytest测试集
    cf.get_value('driver').quit()  # 关闭selenium Chrome driver