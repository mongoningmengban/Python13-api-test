# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""
from common import contants
from common.do_excel import DoExcel
from common.request import Request

# 不用unittest的写法

# 请求不成功
# url data text json
# str dict  eval json
# 接口自动化的流程 写用例--执行用例--报告
do_excel = DoExcel(contants.case_file)  # 传入cases.xlsx
cases = do_excel.get_cases('login')
request = Request()  # 实例化对象
for case in cases:
    print("开始执行第{0}用例".format(case.id))
    # 使用封装好的request 来完成请求
    resp = request.request(case.method, case.url, case.data)
    # 将返回结果和期望结果进行匹配
    if resp.text == case.expected:
        # 一致就写入Excel的结果为PASS，并且
        do_excel.write_result(case.id + 1, resp.text, 'PASS')
        print("第{0}用例执行结果：PASS".format(case.id))
    else:
        do_excel.write_result(case.id + 1, resp.text, 'FAIL')
        print("第{0}用例执行结果：FAIL".format(case.id))
