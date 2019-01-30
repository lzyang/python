# -*- coding: UTF-8 -*-
from gensim import models


# model = models.KeyedVectors.load_word2vec_format("/Users/morningsun/data/word2vec/mhj.bin",binary=True)
# model = models.KeyedVectors.load_word2vec_format("/Users/morningsun/data/word2vec/mhj_gensim.bin",binary=False)
model = models.KeyedVectors.load_word2vec_format("/Users/morningsun/data/word2vec/in_the_name_of_people.bin",binary=False)
# model = models.KeyedVectors.load_word2vec_format("/Users/morningsun/data/word2vec/tlbb_gensim.bin",binary=False)
# print model[u'基地']
similar = model.most_similar([u"沙瑞金"])
for word in similar:
    print word[0],word[1]

for word in similar:
    print (word[0]),