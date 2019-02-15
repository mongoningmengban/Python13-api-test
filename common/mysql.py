# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""
import pymysql

from common.config import ReadConfig


class MysqlUtil:

    def __init__(self):
        # 想想这块如何放到配置文件里面去？？？
        # host = "test.lemonban.com"
        # user = "test"
        # password = "test"
        config = ReadConfig()
        host = config.get('db', 'host')
        user = config.get('db', 'user')
        password = config.get('db', 'pwd')
        port = config.getint('db', 'port')

        # 1,建立连接
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=port)
        # 2，新建一个查询
        self.cursor = self.mysql.cursor()

    def fetch_one(self, sql):
        # 执行SQL
        self.cursor.execute(sql)
        # 获取结果
        result = self.cursor.fetchone()
        return result  # 返回结果

    def close(self):
        self.cursor.close()  # 关闭查询
        self.mysql.close()  # 关闭连接


if __name__ == '__main__':
    mysql = MysqlUtil()
    sql = "select max(mobilephone) from future.member"
    result = mysql.fetch_one(sql)  # 返回的是tuple
    print(result[0])  # 使用下标去获取值
    mysql.close()
