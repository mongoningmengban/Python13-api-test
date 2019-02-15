# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""
import unittest

from ddt import ddt, data

from common import contants
from common.do_excel import DoExcel
from common.mysql import MysqlUtil
from common.request import Request

"""
1,数据库里面查最大的手机号+1
2，case.data 里面的手机号码给特换掉
3，然后再去请求
"""




@ddt
class APITest(unittest.TestCase):
    do_excel = DoExcel(contants.case_file)  # 传入cases.xlsx
    login_cases = do_excel.get_cases('login')  # 获取登录用例
    request = Request()  # 实例化对象

    @unittest.skip("忽略测试，不要运行")
    @data(*login_cases)
    def test_login(self, case):
        print("开始执行第{0}用例".format(case.id))
        # 使用封装好的request 来完成请求
        resp = self.request.request(case.method, case.url, case.data)
        # 将返回结果和期望结果进行匹配
        try:
            self.assertEqual(case.expected, resp.text, "login error ")
            # 一致就写入Excel的结果为PASS，并且
            self.do_excel.write_result('login', case.id + 1, resp.text, 'PASS')
            print("第{0}用例执行结果：PASS".format(case.id))
        except AssertionError as e:
            self.do_excel.write_result('login', case.id + 1, resp.text, 'FAIL')
            print("第{0}用例执行结果：FAIL".format(case.id))
            raise e

    register_cases = do_excel.get_cases('register')  # 获取注册用例
    mysql = MysqlUtil()  # 创建数据连接
    sql = "select max(mobilephone) from future.member"  # 查询最大手机号
    max = mysql.fetch_one(sql)[0]  # 执行SQL，并且返回最近的一条数据，是元祖，使用下标取第一个值
    print(type(max))

    @data(*register_cases)
    def test_register(self, case):
        print("开始执行第{0}用例".format(case.id))
        import json
        data_dict = json.loads(case.data)  # Excel字符串转成字典
        if data_dict['mobilephone'] == '${register_mobile}':  # 判断是否等于标记
            data_dict['mobilephone'] = int(self.max) + 1  # 将最大手机号码+1 赋值给mobilephone
        # 使用封装好的request 来完成请求
        resp = self.request.request(case.method, case.url, data_dict)  # 这里注意要传做过特换的字典！！！！
        # 将返回结果和期望结果进行匹配
        try:
            self.assertEqual(case.expected, resp.text, "register error ")
            # 一致就写入Excel的结果为PASS，并且
            self.do_excel.write_result('register', case.id + 1, resp.text, 'PASS')
            print("第{0}用例执行结果：PASS".format(case.id))
        except AssertionError as e:
            self.do_excel.write_result('register', case.id + 1, resp.text, 'FAIL')
            print("第{0}用例执行结果：FAIL".format(case.id))
            raise e
