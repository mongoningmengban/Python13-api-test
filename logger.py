# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function：
"""
import logging
import logging.handlers
import os

from common import contants

# 输出到文件，文件路径请使用绝对路径 logs
# 输出控制台，定义输出级别debug
# 不同的输出级别可配置


def get_logger(logger_name):

    logger = logging.getLogger(logger_name)
    logger.setLevel('INFO')
    # 定义输出格式
    fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)s]"
    formate = logging.Formatter(fmt)

    file_name = os.path.join(contants.logs_dir, 'case.log')
    file_handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=20 * 1024 * 1024, backupCount=10)
    file_handler.setLevel('INFO')
    file_handler.setFormatter(formate)


    logger.addHandler(file_handler)

    return logger


logger = get_logger(logger_name='invest')
logger.error('this is error ')
