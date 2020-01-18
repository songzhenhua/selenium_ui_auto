# coding=utf-8
# @Time  : 2019/12/22
# @Author: 星空物语
# @File  : conftest.py
# @Description: 1.pytest提供数据、操作共享的文件
#               2.conftest.py文件名是固定的，不可以修改
#               3.conftest.py文件所在目录必须存在__init__.py文件
#               4.其他文件不需要import导入conftest.py，pytest用例会自动查找
#               5.所有同目录测试文件运行前都会执行conftest.py文件

import pytest
from py._xmlgen import html
import config.config as cf
import logging

log = logging.getLogger('szh.conftest')


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """当测试失败的时候，自动截图，展示到html报告中"""
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            driver = cf.get_value('driver')  # 从全局变量取driver
            screen_img = driver.get_screenshot_as_base64()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        report.description = str(item.function.__doc__)#.decode('utf-8', 'ignore')  # 不解码转成Unicode，生成HTML会报错
        # report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    cells.pop()  # 删除报告最后一列links


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.pop()  # 删除报告最后一列links


# @pytest.fixture(scope='function')
# def testcase():
#     log.info(u'\n--------------------用例开始--------------------')
#     yield
#     log.info(u'\n--------------------用例结束--------------------')
