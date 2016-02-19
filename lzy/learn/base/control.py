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