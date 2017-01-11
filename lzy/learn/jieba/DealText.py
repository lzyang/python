# -*- coding: utf8 -*-
__author__ = 'morningsun'
import jieba
import re
# import jieba.posseg as pseg
# pseg.initialize
fn = open("/mdata/code/jupyter/jdw2v.txt","w")
num = 0
err = 0
regex = re.compile("[()（）。\?，\!\|,+\.【】\-/]".decode("utf-8"))
for line in open("/mdata/code/jupyter/jd_title.txt"):
    items = line.split("\t")
    if(len(items)<7):
        err+=1
        print "err data count:%s" % err
        print "err msg:", line
        continue
    prodName = items[5]
    clean = regex.sub(" ", prodName.decode("utf-8"))
    segs = jieba.cut(clean)
    nseg = []
    for seg in segs:
        if seg != " ":
            nseg.append(seg)
    nprodName = " ".join(nseg) + " "
    fn.write(nprodName.encode("utf-8"))
    num += 1
    if(num%1000==0):
        print "dealSize:%s" % num

