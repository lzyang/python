# coding=utf-8
__author__ = 'root'

# tuple和list的主要区别在于，一旦建立，tuple的各个元素不可再变更，而list的各个元素可以再变更。
s1 = (2, 1.3, "str", 5.6, 9, 12, False)
s2 = [True, 5, 'simple']
s3 = [1, [3, 4, 5]]
print s1, type(s1)
print s2, type(s2)
print s3, type(s3)

print s1[0]
print s2[2]
print s3[1][2]

print s1[:5]  # 从开始到下标4 （下标5的元素 不包括在内）

print s1[2:]  # 从下标2到最后

print s1[0:5:2]  # 从下标0到下标4 (下标5不包括在内)，每隔2取一个元素 （下标为0，2，4的元素）

print s1[2:0:-1]  # 从下标2到下标1

print s1[-1]  # 序列最后一个元素

print s1[-3]  # 序列倒数第三个元素

# 字符串是一种特殊的元素，因此可以执行元组的相关操作。

str = 'abcdef'

print str[2:4]

print "==================================================="
nl = [1, 2, 5, 3, 5]
print nl.count(5)  # 计数，看总共有多少个5

print nl.index(3)  # 查询 nl 的第一个3的下标

nl.append(6)  # 在 nl 的最后增添一个新元素6

nl.sort()  # 对nl的元素排序

print nl.pop()  # 从nl中去除最后一个元素，并将该元素返回。

nl.remove(2)  # 从nl中去除第一个2

nl.insert(0, 9)  # 在下标为0的位置插入9

print nl

print [1, 2, 3] + [3, 6, 9]

# ================总结====================
# tuple元素不可变，list元素可变

# 序列的引用 s[2], s[1:8:2]

# 字符串是一种tuple