# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： Requests封装类，使用一个方法解决多种请求方式的调用
"""

import requests

from common.config import ReadConfig




class Request:

    def __init__(self):
        self.session = requests.sessions.session()  # 实例化一个session

    def request(self, method, url, data=None):
        method = method.upper()  # 将字符转成全部大写
        config = ReadConfig()
        pre_url = config.get('api', 'pre_url')  # 拼接
        url = pre_url + url  # URL拼接
        if data is not None and type(data) == str:
            data = eval(data)  # 如果是字符串就转成字典
        # log.info('method: {0}  url: {1}'.format(method, url))
        # log.info('data: {0}'.format(data))
        if method == 'GET':
            resp = self.session.request(method, url=url, params=data)  # 调用get方法，使用params传参
            # log.info('response: {0}'.format(resp.text))
            return resp

        elif method == 'POST':
            resp = self.session.request(method, url=url, data=data)  # 调用post方法，使用data传参
            # log.info('response: {0}'.format(resp.text))
            return resp
        else:
            # log.error('Un-support method !!!')
            pass

    def close(self):
        self.session.close()  # 关闭session
