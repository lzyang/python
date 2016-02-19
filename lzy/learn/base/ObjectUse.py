# -*- coding: utf8 -*-
__author__ = 'morningsun'


class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'

    #self，它是为了方便我们引用对象自身。方法的第一个参数必须是self，无论是否用到
    def move(self, dx, dy):
        print self.way_of_reproduction
        position = [0,0]
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return position

summer = Bird()
print summer.way_of_reproduction

# 调用move方法的时候，我们只传递了dx和dy两个参数，不需要传递self参数（因为self只是为了内部使用）。
print summer.move(3,5)


class Chicken(Bird):
    way_of_move = 'walk'
    possible_in_KFC = True


class Oriole(Bird):
    way_of_move = 'fly'
    possible_in_KFC = False


summer = Chicken()
print summer.have_feather
print summer.move(5, 8)

# __init__()是一个特殊方法(special method)。Python有一些特殊方法。Python会特殊的对待它们。特殊方法的特点是名字前后有两个下划线。
#
# 如果你在类中定义了__init__()这个方法，创建对象时，Python会自动调用这个方法。这个过程也叫初始化。

class happyBird(Bird):
    def __init__(self, more_words):
        print 'We are happy birds.', more_words

summer = happyBird('Happy,Happy!')