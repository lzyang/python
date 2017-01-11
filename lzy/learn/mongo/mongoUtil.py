# -*- coding: utf8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

__author__ = 'morningsun'

from pymongo import MongoClient

client = MongoClient("127.0.0.1",111)
coll = client.jd_all_product.jd_productAll20160922
cur = coll.find()

list = []
count = 0
total_count = 0
for item in cur:
    pre = ""
    total_count += 1
    for cb in item.get("metaDataList").get("product_info"):
        if(pre==u'品牌'):
            print 'No.',total_count,'  ',cb
            list.append(cb)
        pre = cb

print "total_count", total_count
s = set(list)
fn = open("/mdata/code/jupyter/jd_brand.txt","w")
for b in s:
    fn.write(b+"\n")