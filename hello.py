"""
# 输出1000内的斐波那契数列
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b
"""
import os
from collections import Iterable

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
languages = ['C', 'C++', 'Java', "php", "python"]
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
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


g2 = fib(6)
# for循环生成器拿不到return值'done'
# for item in g2:
#     print(item)

# 通过捕获异常来获取return值
while True:
    try:
        x = next(g2)
        print(x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
