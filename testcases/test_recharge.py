# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""
import unittest

from libext.ddtnew import ddt, data

from common import contants
from common.do_excel import DoExcel
# 1，excel 里面设计第一条case是正常登陆
# 2，session 保持会话的方式来进行请求的话，那就需要把你这个request的实例化的对象放到类里面
# 3，获取Excel数据，运行用例
from common.request import Request


@ddt
class RechargeTest(unittest.TestCase):
    do_excel = DoExcel(contants.case_file)  # 传入cases.xlsx
    cases = do_excel.get_cases('recharge')

    @classmethod
    def setUpClass(cls): # 每个测试类里面去运行的操作放到类方法里面
        print("\n这是一个类方法")
        cls.request = Request()  # 实例化对象

    def setUp(self):  # 每个测试方法里面去运行的操作放到类方法里面
        print("这是一个setUP")
        pass

    @data(*cases)
    def test_recharge(self, case):
        print("开始执行第{0}用例".format(case.id))
        # 使用封装好的request 来完成请求
        resp = self.request.request(case.method, case.url, case.data)
        # 将返回结果和期望结果进行匹配
        try:
            self.assertEqual(case.expected, resp.json()['code'], "recharge error ")
            # 一致就写入Excel的结果为PASS，并且
            self.do_excel.write_result('recharge', case.id + 1, resp.text, 'PASS')
            print("第{0}用例执行结果：PASS".format(case.id))
        except AssertionError as e:
            self.do_excel.write_result('recharge', case.id + 1, resp.text, 'FAIL')
            print("第{0}用例执行结果：FAIL".format(case.id))
            raise

    @classmethod
    def tearDownClass(cls):
        cls.request.close()  # 关闭session
