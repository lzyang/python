# -*- coding: utf8 -*-
__author__ = 'morningsun'

dic = {'lilei': 90, 'lily': 100, 'sam': 57, 'tom': 90}
for key in dic:
    print key, dic[key]

print "====================================="

dic["aaa"] = 120

for key in dic:
    print key, dic[key]

# 词典的常用方法

print dic.keys()           # 返回dic所有的键

print dic.values()         # 返回dic所有的值

print dic.items()          # 返回dic所有的元素（键值对）

# dic.clear()                # 清空dic，dict变为{}

print "==============================>>"
for x in dic.items():
    print "==\t==" + str(x[0]) + str(x[1])