# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""
import re

admin_user = '15873171553'
admin_pwd = '123456'

data = {"admin_user": "15873171553", "admin_pwd": "123456"}
s = '{"mobilephone":"${admin_user}","pwd":"${admin_pwd}"}'
p = "\$\{admin_user}"  # 原本字符的写法
p1 = "\$\{(.*?)}"  # 元字符和限定符，（）代表组 英文输入法下面去写正则表达式
m = re.search(p1, s)  # 任意位置开始找，找到一个就返回match
print("任意位置开始找，找到一个就返回match", m)
g = m.group()  # 返回的是整个匹配的字符串
print(g)
g1 = m.group(1)  # 取一个组的匹配字符串
print(g1)  #
value = data[g1]
s = re.sub(p1, value, s)  # 查找全部
print("使用正则表达式查找，并且替换", s)

l = re.findall(p1, s)  # 查找全部，返回一个列表
print("查找全部，返回一个列表", l)

# # 将字符串转成字典，然后根据KEY去取值，取到值判断是否需要替换
# dict1 = json.loads(s)
# if dict1['mobilephone'] == '${admin_user}':
#     dict1['mobilephone'] = admin_user
#
# if dict1['pwd'] == '${admin_pwd}':
# #     dict1['pwd'] = admin_pwd
#
# print(dict1)


# 字符串的查找，替换
if s.find('${admin_user}') > -1:
    s = s.replace('${admin_user}', admin_user)  # 重新去赋值

if s.find('${admin_pwd}') > -1:
    s = s.replace('${admin_pwd}', admin_pwd)

print(s)

# 根据key,动态的去取值
