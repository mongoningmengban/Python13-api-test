# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 配置文件类
"""
import configparser

from common import contants


# # 实例化对象
# config = configparser.ConfigParser()
# # 加载文件
# config.read(contants.global_conf)  # 先加载开关的配置
# open = config.getboolean('switch', 'open')
# print(type(open), open)
# if open:
#     config.read(contants.test_conf)  # open是True
# else:
#     config.read(contants.test2_conf)  # open是False
#
# value = config.get('api', 'pre_url')
# print(type(value), value)


#
# # 实例化对象
# config = configparser.ConfigParser()
# # 加载文件
# config.read(contants.test2_conf)  # open是True
#
# switch = config.getboolean('api', 'switch')
# if switch:
#     url = config.get('api', 'pre_url1')
#     host = config.get('db', 'host1')
# else:
#     url = config.get('api', 'pre_url2')
#     host = config.get('api', 'host2')


class ReadConfig:

    def __init__(self):
        # 实例化对象
        self.config = configparser.ConfigParser()
        # 加载文件
        self.config.read(contants.global_conf, encoding='utf-8')  # 先加载开关的配置
        open = self.config.getboolean('switch', 'open')  # 总开关

        # 灵活切换测试环境
        if open:  # 如果是True就加载 test.conf
            self.config.read(contants.test_conf, encoding='utf-8')  # open是True
        else:  # 如果是False 就加载 test2.conf
            self.config.read(contants.test2_conf, encoding='utf-8')  # open是False

    def get(self, section, option):
        return self.config.get(section, option)

    def getboolean(self, section, option):
        return self.config.getboolean(section, option)

    def getint(self, section, option):
        return self.config.getint(section, option)
