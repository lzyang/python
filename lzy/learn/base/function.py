# -*- coding: utf8 -*-
__author__ = 'morningsun'


# 在Python中，当程序执行到return的时候，程序将停止执行函数内余下的语句。return并不是必须的，当没有return, 或者return后面没有返回值时，函数将自动返回None。
# None是Python中的一个特别的数据类型，用来表示什么都没有，相当于C中的NULL。None多用于关键字参数传递的默认值

#return可以返回多个值，以逗号分隔。相当于返回一个tuple(定值表)。
#
# 对于基本数据类型的变量，变量传递给函数后，函数会在内存中复制一个新的变量，从而不影响原来的变量。（我们称此为值传递）
#
# 但是对于表来说，表传递给函数的是一个指针，指针指向序列在内存中的位置，在函数中对表的操作将在原有内存中进行，从而影响原有变量。 （我们称此为指针传递）

def square_sum(a,b):
    c = a**2 + b**2
    return c,3

print square_sum(1,2)


# 包裹传递
print "=============包裹传递================"


def func(*name):
    print type(name)
    print name

func(1, 4, 6)
func(5, 6, 7, 1, 2, 3)


def func(**dict):
    print type(dict)
    print dict

func(a=1, b=9)
func(m=2, n=1, c=11)

# 解包裹
print "=============解包裹================"

def func(a, b, c):
    print a, b, c

args = (1, 3, 4)
func(*args)

dict = {'a': 1, 'b': 2, 'c': 3}
func(**dict)
