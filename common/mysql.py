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

    def __init__(self, return_dict=False):
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
        if return_dict:
            self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor)  # 指定每行数据以字典的形式返回
        else:
            self.cursor = self.mysql.cursor()  # 指定每行数据以元祖的形式返回

    def fetch_one(self, sql):
        # 执行SQL
        self.cursor.execute(sql)
        # 获取结果
        result = self.cursor.fetchone()  # 返回元祖（）
        return result  # 返回结果

    def fetch_all(self, sql):
        # 执行SQL
        self.cursor.execute(sql)
        # 获取结果
        results = self.cursor.fetchall()  # 返回列表 [(),()]
        return results

    def close(self):
        self.cursor.close()  # 关闭查询
        self.mysql.close()  # 关闭连接


if __name__ == '__main__':
    # mysql = MysqlUtil()
    # sql = "select max(mobilephone) from future.member"
    # result = mysql.fetch_one(sql)  # 返回的是tuple
    # print(result[0])  # 使用下标去获取值
    # mysql.close()

    mysql = MysqlUtil(return_dict=True)
    sql = "select * from future.member limit 10"
    results = mysql.fetch_all(sql)  # 返回的是列表里面放字典
    for result in results:
        print(result['Id'])
    mysql.close()
