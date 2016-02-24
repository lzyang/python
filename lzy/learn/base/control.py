# -*- coding: utf8 -*-
__author__ = 'morningsun'

if 1 < 0:
    print True
print False

print "======================================================="
i = 1

if i > 0:
    print 'positive i'
    i = i + 1
elif i == 0:
    print 'i is 0'
    i = i * 10
else:
    print 'negative i'
    i = i - 1

print 'new i:', i

print "======================================================="

for a in [3, 4.4, 'life']:
    print a

idx = range(5)
print idx

for a in range(10):
    print a ** 2

while i < 10:
    print i
    i = i + 1

print "====================================================="

for i in range(10):
    if i == 6:
        break
    elif i==3:
        continue
    print i


# 在该例子中，我们利用len()函数和range()函数，用i作为S序列的下标来控制循环。在range函数中，分别定义上限，下限和每次循环的步长。这就和C语言中的for循环相类似了。
S = 'abcdefghijk'
for i in range(0, len(S), 2):
    print S[i]

# enumerate()在每次循环中，返回的是一个包含两个元素的定值表(tuple)，两个元素分别赋予index和char
S = 'abcdefghijk'
for (index,char) in enumerate(S):
    print index
    print char

# 如果你多个等长的序列，然后想要每次循环时从各个序列分别取出一个元素，可以利用zip()方便地实现：
ta = [1, 2, 3]
tb = [9, 2, 7]
tc = ['a', 'b', 'c']
for (a, b, c) in zip(ta, tb, tc):
    print(a, b, c)