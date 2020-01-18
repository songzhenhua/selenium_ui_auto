# coding=utf-8
# @Time  : 2020/1/12 18:05
# @Author: zhenhua.song
# @File  : log.py
# @Description: 封装日志功能

import logging
import time
import config.config as cf


class Logger(object):
    """封装的日志模块"""

    def __init__(self, logger, cmd_level=logging.DEBUG, file_level=logging.DEBUG):
        try:
            self.logger = logging.getLogger(logger)
            self.logger.setLevel(logging.DEBUG)  # 设置日志输出的默认级别
            '''pytest报告可以自动将log整合进报告，不用再自己单独设置保存
            # 日志输出格式
            fmt = logging.Formatter(
                '%(asctime)s[%(levelname)s]\t%(message)s')
            # 日志文件名称
            curr_time = time.strftime("%Y-%m-%d %H.%M.%S")
            log_path = cf.get_value('log_path')
            self.log_file = '{}log{}.txt'.format(log_path, curr_time)
            # 设置控制台输出
            sh = logging.StreamHandler()
            sh.setFormatter(fmt)
            sh.setLevel(cmd_level)
            # 设置文件输出
            fh = logging.FileHandler(self.log_file)
            fh.setFormatter(fmt)
            fh.setLevel(file_level)
            # 添加日志输出方式
            self.logger.addHandler(sh)
            self.logger.addHandler(fh)
            '''
        except Exception as e:
            raise e

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def error(self, msg):
        self.logger.error(msg)

    def warning(self, msg):
        self.logger.warning(msg)
