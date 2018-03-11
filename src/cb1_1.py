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

# zip()函数：zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。\
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
a = [1, 2, 3]
b = [4, 5, 6]
c = zip(a, b)
for v in c:
    print(v)
origin = zip(*c)
for v in origin:
    print(v)

# 利用zip()可以反转字典k和v
dic1 = {"a": 1, "b": 2, "c": 3}
dic2 = zip(dic1.values(), dic1.keys())
print('-' * 10, end='\n')
print(min(dic2),end='\n')
print('-'*10,end='\n')
a,*b = zip(dic1.values(), dic1.keys())
print(a,*b,end='-'*10+'\n')

# 在两个字典中寻找相同点：集合操作
print('在两个字典中寻找相同点\n')
dic3 = {'a':2,'b':5,'d':3}
print(dic1.keys() & dic3.keys())
print(dic1.keys()-dic3.keys())
a={key:dic1[key] for key in dic1.keys()-{'a'}}
print(a)

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
a=[1,2,2,3,4,5,6,3,8,5,9]
print(list(dedupe(a)))

print('-'*10)
a=[{'x':1,'y':2},{'x':1,'y':3},{'x':1,'y':2},{'x':2,'y':4}]
key = lambda d:(d['x'],d['y'])
print(key(a[0]))


class strandrepr(object):
    def __init__(self,id):
        self.id = id
    def __repr__(self):
        print('repr called')
        return 'user({})'.format(self.id)
    def __str__(self):
        print('str called')
        return 'User({})'.format(self.id)

c= strandrepr(10)
print(c)

s = ('acd',1,'eof',23,'fd')
print(','.join(str(x) for x in s))