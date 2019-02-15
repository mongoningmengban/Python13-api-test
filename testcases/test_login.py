# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""

import unittest

from libext.ddt import ddt, data

from common import contants
from common.do_excel import DoExcel
from common.request import Request
import logger

logger = logger.get_logger(logger_name='LoginTest')
# 一个接口一个类，一个类一个方法
# 一个类，多个方法，多个接接口
# 一个类，一个方法，全部接口 -------


@ddt
class LoginTest(unittest.TestCase):
    do_excel = DoExcel(contants.case_file)  # 传入cases.xlsx
    cases = do_excel.get_cases('login')
    request = Request()  # 实例化对象

    def setUp(self):
        pass

    @data(*cases)
    def test_login(self,case):
        logger.info("开始执行第{0}用例".format(case.id))
        # 使用封装好的request 来完成请求
        resp = self.request.request(case.method, case.url, case.data)
        # 将返回结果和期望结果进行匹配
        try:
            self.assertEqual(case.expected, resp.text, "login error ")
            # 一致就写入Excel的结果为PASS，并且
            self.do_excel.write_result('login',case.id + 1, resp.text, 'PASS')
            logger.info("第{0}用例执行结果：PASS".format(case.id))
        except AssertionError as e:
            self.do_excel.write_result('login',case.id + 1, resp.text, 'FAIL')
            logger.error("第{0}用例执行结果：FAIL".format(case.id))
            raise e

    def tearDown(self):
        pass

