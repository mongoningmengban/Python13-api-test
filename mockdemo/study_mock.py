# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""
from unittest import mock

import requests


def request_baidu():
    # 抓百度的内容
    return requests.get('https://www.baidu.com').text.encode('utf-8')


def print_baidu():
    print(request_baidu())


request_baidu = mock.Mock(return_value='this is baidu.')
print_baidu()
