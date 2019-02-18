# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""

import unittest

from common import contants
from common.do_excel import DoExcel
from common.mysql import MysqlUtil
from common.request import Request
from libext.ddtnew import ddt, data


@ddt
class RegisterTest(unittest.TestCase):
    do_excel = DoExcel(contants.case_file)  # 传入cases.xlsx
    cases = do_excel.get_cases('register')
    request = Request()  # 实例化对象

    def setUp(self):
        self.mysql = MysqlUtil(return_dict=True)  # 创建数据连接
        sql = "select max(mobilephone) as max_phone from future.member"  # 查询最大手机号
        self.max = self.mysql.fetch_one(sql)['max_phone']  # 执行SQL，并且返回最近的一条数据，是元祖，使用下标取第一个值

    @data(*cases)
    def test_register(self, case):
        print("开始执行第{0}用例".format(case.id))
        # 替换手机号码
        data = case.data  # excel里面读取出来是字符串
        # 字符串的查找并替换
        # if data.find('${register_mobile}') > -1:
        #     data.s.replace('${register_mobile}', self.max)

        # 字典，根据KEY取值，然后判断，是否需要替换
        import json
        data = json.loads(data)
        if data['mobilephone'] == '${register_mobile}':
            data['mobilephone'] = int(self.max) + 1

        # 使用封装好的request 来完成请求
        resp = self.request.request(case.method, case.url, data)  # 这里data传str或者dict都OK ,因为方法里面会做判断
        # 将返回结果和期望结果进行匹配
        try:
            self.assertEqual(case.expected, resp.text, "register error ")
            if resp.json()['msg'] == '注册成功':
                sql = 'select * from future.member where mobilephone = {0}' \
                    .format(data['mobilephone'])
                results = self.mysql.fetch_all(sql)
                # 首先判断是否有成功插入数据
                self.assertEqual(1, len(results))
                member = results[0]  # 获取到这一条数据,是一个字典
                self.assertEqual(0, member['LeaveAmount'])  # 判断注册成功余额应该是0
            # 一致就写入Excel的结果为PASS，并且
            self.do_excel.write_result("register", case.id + 1, resp.text, 'PASS')
            print("第{0}用例执行结果：PASS".format(case.id))
        except AssertionError as e:
            self.do_excel.write_result("register", case.id + 1, resp.text, 'FAIL')
            print("第{0}用例执行结果：FAIL".format(case.id))
            raise e

    def tearDown(self):
        self.mysql.close()
