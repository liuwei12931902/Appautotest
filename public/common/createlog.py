# import logging
# from logging import *
# import os
# import time
# from config.globelsetting import log_path
#
#
# class Runlogger(object):
#
#     def __init__(self):
#         '''
#         指定日志的级别
#         将日志存放着指定的目录
#         :param level:
#         :param logger:
#         '''
#         # if level == 'info':
#         #     setloglevel = logging.INFO
#         # elif level == 'debug':
#         #     setloglevel = logging.DEBUG
#         # elif level == 'warning':
#         #     setloglevel = logging.WARNING
#         # elif level == 'error':
#         #     setloglevel = logging.ERROR
#         # else:
#         #     pass
#         # 设置日志文件的名称
#         log_file = os.path.join(log_path, '{0}.log-xz'.format(time.strftime('%Y-%m-%d')))
#         # 实例化logging 类
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#
#         # 创建一个handler，用于写入日志文件
#         fh = logging.FileHandler(log_file, mode='w')
#         fh.setLevel(logging.DEBUG)
#
#         # 创建一个handler，用于输出控制台
#         ch = logging.StreamHandler()
#         ch.setLevel(logging.INFO)
#
#         # 定义一个handle的格式
#         formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#         fh.setFormatter(formatter)
#         ch.setFormatter(formatter)
#
#         # 给logger添加handler
#         logger.addHandler(fh)
#         logger.addHandler(ch)
#
#
# # **************************
# # 使用方法
# # runlog =  Runlogger('info'，)
# # runlog.get_log()
# # logger.info()
# # **************************
#
#
# runlog = Runlogger()
# runlog

#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# log_4_func.py
# log的工程应用
# author: De8uG

import logging
from config import globelsetting
import time
import os
"""
工程使用需求：
1-不同日志名称
2-打印同时在控制台，也有文件
3-灵活控制等级
"""


class Runlogger(object):

    def debug_log(self, logger_name='DEBUG-LOG', level=logging.DEBUG):
        # 创建 logger对象
        logger = logging.getLogger(logger_name)
        logger.setLevel(level)  # 添加等级

        # 创建控制台 console handler
        ch = logging.StreamHandler()
        ch.setLevel(level)

        # 创建文件 handler
        log_file = os.path.join(globelsetting.log_path, '{0}.log'.format(time.strftime('%Y-%m-%d')))
        fh = logging.FileHandler(filename=log_file, encoding='utf-8')

        # 创建 formatter
        formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(name)s %(levelname)s %(message)s')

        # 添加 formatter
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        # 把 ch， fh 添加到 logger
        logger.addHandler(ch)
        logger.addHandler(fh)

        return logger


# def main():
#     # 测试
#     logger = debug_log.de8ug_log()
#     logger.debug('debug message')
#     logger.info('info message')
#     logger.warning('warn message')
#     logger.error('error message')
#     logger.critical('critical message')
#
#
# if __name__ == "__main__":
#     main()




