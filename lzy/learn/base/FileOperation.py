# -*- coding: utf8 -*-
__author__ = 'morningsun'


# 我们打开一个文件，并使用一个对象来表示该文件：
# f = open(文件名，模式)
#
# 最常用的模式有：
# "r"     # 只读
# “w”     # 写入

f = open("/mdata/codedata/python/testFile.txt","r")

print f.read(100)  # 读取N bytes的数据
print "=================================="
print f.readline()       # 读取一行
print "=================================="
print f.readlines()      # 读取所有行，储存在列表中，每个元素是一行。
print "=================================="

#f.write('python language is good')

f.close()

moives={}
for line in open("/mdata/codedata/python/ml-latest-small/movies.csv"):
    if line.find("|")>0:
        (id,title) = line.split("|")[0:2]
        moives[id] = title

for (id,title) in moives.items():
    print id,title