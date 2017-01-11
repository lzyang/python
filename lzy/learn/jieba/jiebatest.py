# -*- coding: utf8 -*-
__author__ = 'morningsun'
import jieba
import jieba.posseg as pseg

seg_list = jieba.cut("我来到北京青华大学",cut_all=True)  #全切分模式
print "Full Mode:", "/ ".join(seg_list)
seg_list = jieba.cut("我来到北京青华大学",cut_all=False)  #精确模式
print "Default Mode:", "/ ".join(seg_list)

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print ", ".join(seg_list)

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print ", ".join(seg_list)


words = pseg.cut("我爱北京天安门")
for w in words:
    print w.word, w.flag