# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""

# 先自行安装这个模块 pip install pymysql
import pymysql
# 1, 建立连接，
host = "test.lemonban.com"
user = "test"
password = "test"
mysql = pymysql.connect(host=host, user=user, password=password, port=3306)
# 2，新建一个查询页面
cursor = mysql.cursor()
# 3，编写SQL
sql = "select max(mobilephone) from future.member"
# 4，执行SQL
cursor.execute(sql)
# 5，查看结果
result = cursor.fetchone()
print(result[0])
# 6,关闭查询
cursor.close()
# 7,数据库连接关闭
mysql.close()


