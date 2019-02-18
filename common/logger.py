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
from common.config import ReadConfig

# 输出到文件，文件路径请使用绝对路径 logs
# 输出控制台，定义输出级别debug
# 不同的输出级别可配置
config = ReadConfig()


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel('DEBUG') # 直接设置为最低
    # 定义输出格式
    fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)s]"
    formate = logging.Formatter(fmt)

    file_name = os.path.join(contants.logs_dir, 'case.log')
    file_handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=20 * 1024 * 1024, backupCount=10)
    level = config.get('log', 'file_handler')
    file_handler.setLevel(level)
    file_handler.setFormatter(formate)

    console_handler = logging.StreamHandler()
    level = config.get('log', 'console_handler')
    console_handler.setLevel(level)
    console_handler.setFormatter(formate)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


if __name__ == '__main__':
    logger = get_logger(logger_name='invest')
    logger.error('this is error ')
    logger.info('this is info ')
    logger.debug('this is debug ')
