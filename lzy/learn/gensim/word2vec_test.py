# -*- coding: utf-8 -*-
# import modules & set up logging
import logging
import os
from gensim.models import word2vec

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences = word2vec.LineSentence('/Users/morningsun/data/word2vec/mhj_jieba.txt')
# sentences = word2vec.LineSentence('/Users/morningsun/data/word2vec/in_the_name_of_people_segment.txt')

model = word2vec.Word2Vec(sentences, hs=1,min_count=1,window=3,size=100)

# model = word2vec.Word2Vec(sentences, size=100, window=3, min_count=3, sg=1, iter=10, negative=20)

print "------------train finish--------------"
print u"------------similar 沙瑞金--------------"


req_count = 10
for key in model.wv.similar_by_word('纪宁'.decode('utf-8'), topn =100):
    # if len(key[0])==3:
        req_count -= 1
        print key[0], key[1]
        if req_count == 0:
            break

# print "------------similarity--------------"
#
# print model.wv.similarity('沙瑞金'.decode('utf-8'), '高育良'.decode('utf-8'))
# print model.wv.similarity('李达康'.decode('utf-8'), '王大路'.decode('utf-8'))
#
# print "------------match--------------"
#
# print model.wv.doesnt_match(u"沙瑞金 高育良 李达康 刘庆祝".split())