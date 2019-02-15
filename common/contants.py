# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 常量
"""
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目根路径
# print(base_dir)
data_dir = os.path.join(base_dir, "datas")  # datas文件夹路径

case_file = os.path.join(data_dir, "cases.xlsx")  # case.xlsx文件路径
# print(case_file)

conf_dir = os.path.join(base_dir, "conf")

test_conf = os.path.join(conf_dir, "test.conf")  # 测试配置文件路径
test2_conf = os.path.join(conf_dir, "test2.conf")  # 测试配置文件路径
global_conf = os.path.join(conf_dir, "global.conf")  # 测试配置文件路径

logs_dir = os.path.join(base_dir, "logs")

testcases_dir = os.path.join(base_dir, "testcases")

reports_dir = os.path.join(base_dir, 'reports')  # reports文件夹路径
reports_html = os.path.join(reports_dir, 'reports.html')  # reports文件夹路径