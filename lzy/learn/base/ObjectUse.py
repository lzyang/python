# -*- coding: utf8 -*-
__author__ = 'morningsun'


class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'

    #self，它是为了方便我们引用对象自身。方法的第一个参数必须是self，无论是否用到
    def move(self, dx, dy):
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