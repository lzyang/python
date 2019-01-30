import fasttext


import fasttext

# 训练模型
classifier = fasttext.supervised("train.txt", "model", label_prefix="__label__", dim=100, epoch=2, word_ngrams=1, min_count=1, lr=0.1, bucket=200000)