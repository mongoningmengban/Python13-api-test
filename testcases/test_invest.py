# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""
import unittest

from common import contants
from common import context
from common import logger
from common.context import Context
from common.do_excel import DoExcel
from common.mysql import MysqlUtil
from common.request import Request
from libext.ddtnew import ddt, data

logger = logger.get_logger(logger_name='case')  # 获取logger实例


@ddt
class InvestTest(unittest.TestCase):
    do_excel = DoExcel(contants.case_file)  # 传入cases.xlsx
    cases = do_excel.get_cases('invest')

    @classmethod
    def setUpClass(cls):  # 每个测试类里面去运行的操作放到类方法里面
        logger.debug("\n这是一个类方法")
        cls.request = Request()  # 实例化对象
        cls.mysql = MysqlUtil()

    def setUp(self):  # 每个测试方法里面去运行的操作放到类方法里面
        logger.debug("这是一个setUP")
        pass

    @data(*cases)
    def test_invest(self, case):
        # log.info("开始执行第{0}用例".format(case.id))
        # 查找参数化的测试数据，动态替换
        data_new = context.replace_new(case.data)  # Str测试数据
        # 使用封装好的request 来完成请求
        resp = self.request.request(case.method, case.url, data_new)
        # 将返回结果和期望结果进行匹配
        try:
            self.assertEqual(case.expected, resp.json()['code'], "invest error ")
            # 一致就写入Excel的结果为PASS，并且
            self.do_excel.write_result('invest', case.id + 1, resp.text, 'PASS')
            # log.info("第{0}用例执行结果：PASS".format(case.id))
            # 判断是否加标成功，如果成功就按照借款人ID去数据库查询最新标的记录
            if resp.json()['msg'] == '加标成功':
                loan_member_id = getattr(Context, 'loan_member_id')
                sql = "select id from future.loan where memberID='{0}'" \
                      " order by createTime desc limit 1".format(loan_member_id)
                loan_id = self.mysql.fetch_one(sql)[0]
                setattr(Context, 'loan_id', str(loan_id))  # 记得转成str，后续通过正则替换

        except AssertionError as e:
            self.do_excel.write_result('invest', case.id + 1, resp.text, 'FAIL')
            logger.error("第{0}用例执行结果：FAIL".format(case.id))
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.request.close()  # 关闭session
        cls.mysql.close()  # 关闭MySQL
