#!/bin/bash

"""
cookbook1.1:将序列分解为单独的变量
"""


def hello_world():
    """
    输出helloworld
    """
    print("hello world")


# if __name__ == "__main__":
#     # 输出注释
#     import cb1_1
#     print(help(cb1_1))

# 任何序列都可以通过一个简单的赋值来分解为单独的变量
p = (4, 5, 6)
a, b, c = p
print(a, b, c, end="\n")

# 取出中间任意数量的值,*表达式不能单独存在
q = [1, 2, 3, 4, 5]
d, *e, f = q
print(d, *e, f, end="\n")

# 丢弃某些特定的值
r = (6, 3, 7, 4)
_, g, h, _ = r
print(g, h, end="\n")

# for多变量循环
s = [("hi", "ddd", "dfadf")]
for tag, *param in s:
    print(tag, *param)

# 丢弃连续特定的值
*_, g = r
print(g, "-" * 10)

# collections.deque,deque(maxlen=N)生成一个固定长度的队列，当有新纪录加入时而队列已满，会自动移除最老的记录
from collections import deque

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
for i in q:
    print(i)
print(q, "-" * 10, end="\n")
q.append(4)
q.append(5)
print(q, "-" * 10, end="\n")
q.appendleft(6)
q.pop()
print(q, "-" * 10, end="\n")

# 找出集合中最大最小的元素,heapq模块
import heapq

nums = [1, 2, 3, 4, 5, 6, 4, 3, 8, 43, 0]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))
# 接受一个key，自定义排序
profile = [{"name": "zhi", "price": 101}, {"name": "lrr", "price": 99}]
print(heapq.nlargest(1, profile, key=lambda s: s["price"]))

# 创建一键多值变量 defaultdic
from _collections import defaultdict

tempd = defaultdict(list)
tempd['a'].append(1)
tempd['a'].append(2)
tempd['b'].append(3)
for key in tempd:
    print(tempd[key])

# 让字典保持有序，OrderedDict，内部维护了一个双向链表，大小是普通字典的2倍多
# 应用场景实例，在进行Json编码时精确控制各字段的顺序，那么首先在OrderedDict中构建数据就可以了
from _collections import OrderedDict

od = OrderedDict()
od['foo'] = 1
od['ds'] = 2
od['rt'] = 3
for key in od:
    print(od[key])
zip()