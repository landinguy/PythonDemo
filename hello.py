"""
# 输出1000内的斐波那契数列
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b
"""
import json
import os
from datetime import datetime, timedelta

import mysql.connector
import requests

"""
for循环
languages = ['C', 'C++', 'Java', "php", "python"]
for i in languages:
    print(i)
"""
# print(r'\\\t\\')
# print('line1\nline2\nline3')

# a = 'abc'
# b = a
# a = 'def'
# print('a->' + a)
# print('b->' + b)

''' 两个set可以做交集并集 '''
# s1 = set([1, 2, 3, 4])
# s2 = set([2, 3, 4, 5])
# print(s1 & s2)
# print(s1 | s2)

''' 函数 '''
# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x
#
#
# print(my_abs(9), my_abs(-9))

''' 切片 '''
# languages = ['C', 'C++', 'Java', "php", "python"]
# print(languages[1:4])  # 取索引1-3的值，不包括4
# print(list(range(10)))

# print(isinstance('java', Iterable))  # 判断一个对象是否可迭代

''' 列表生成式 '''
# print([x * x for x in range(1, 11)])
# print([x * x for x in range(1, 11) if x % 2 == 0])
# print([m + n for m in 'ABC' for n in 'XYZ'])
# print([d for d in os.listdir('E:/vueProject')])  # os.listdir可以列出文件和目录

''' generator生成器 '''

# g = (x for x in range(10))
# for item in g:
#     print(item)


# 定义一个生成器
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'


# g2 = fib(6)
# for循环生成器拿不到return值'done'
# for item in g2:
#     print(item)

# 通过捕获异常来获取return值
# while True:
#     try:
#         x = next(g2)
#         print(x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break

''' lambda '''
# print(list(map(lambda x: x * x, range(10))))

''' 面向对象 '''

# class Student(object):
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def print_info(self):
#         print('%s->%s' % (self.__name, self.__age))
#
#
# stu = Student('jack', 18)
# stu.print_info()

''' io操作 '''
# with open('D:/test.txt', 'r') as f:
#     with open('D:/test1.txt', 'a+') as t:
#         for line in f.readlines():
#             t.writelines(line)

''' os '''
# print(os.name)
# print(os.path.abspath('.'))
# print([x for x in os.listdir('d:/')])

''' datetime '''
# print(datetime.now())
# dt = datetime(2019, 1, 23, 10, 40)
# ts = dt.timestamp()
# print(dt, ts, datetime.fromtimestamp(ts), dt + timedelta(days=1))

''' namedtuple '''
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1, 2)
# print(p, p.x, p.y)

''' Counter '''
# c = Counter()
# for ch in 'landing guy':
#     c[ch] = c[ch] + 1
# print(c)

''' requests '''
# r = requests.get('https://www.baidu.com/')
# print(r.status_code)
# params = {'username': 'python1', 'password': 'python1'}
# resp = requests.post('http://192.168.5.114:8084/addUser', json=params)
# print(resp.json())

''' 连接mysql '''
# connect = mysql.connector.connect(user='root', password='root', database='tw')
# cursor = connect.cursor()
# cursor.execute('select * from user where username=%s', ('landinguy',))
# result = cursor.fetchall()
# print(result)
# cursor.close()
# connect.close()

from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

''' SQLAlchemy '''
# 创建对象的基类:
# Base = declarative_base()
#
#
# class User(Base):
#     # 表的名字:
#     __tablename__ = 'user'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     username = Column(String(20))
#     password = Column(String(20))
#
#
# # 初始化数据库连接:
# engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/tw')
# # 创建DBSession类型:
# DBSession = sessionmaker(bind=engine)
# # 创建session对象:
# session = DBSession()
#
# user = User(username='python3', password='python3')
# session.add(user)
# session.commit()
# session.close()



''' 序列化 '''
# d = dict(name='jack', age='18', sex='man')
# jsonStr = json.dumps(d)
# print(jsonStr)
# print(json.loads(jsonStr))
