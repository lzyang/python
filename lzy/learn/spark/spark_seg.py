# -*- coding:utf-8 -*-

import sys
import jieba
from pyspark import SparkConf,SparkContext

sec_dic_path = ""


def to_seg(line):
    # if not jieba.dt.initialized:
    #     urlArr = sec_dic_path.strip().split("/")
    #     jieba.load_userdict(urlArr[-1])

    query = line
    query_words = jieba.cut(query, cut_all=False)
    querys = [w for w in query_words]
    return ",".join(querys)


def line_format(line):
    items = line.split("[##]")
    id = items[0]
    country = items[1]
    appref = items[2]
    pubref = items[3]
    applicant = items[4]
    ipc = items[5]
    type = items[6]
    reference = items[7]
    title = items[8]
    abs = items[9]
    claim = items[10]
    des = items[11]

    title_seg = to_seg(title)
    abs_seg = to_seg(abs)
    claim_seg = to_seg(claim)
    des_seg = to_seg(des)


    str = id + "[##]" + country + "[##]" + appref + "[##]" + pubref + "[##]" + applicant + "[##]" + ipc + "[##]" + type + "[##]" + reference + "[##]" + title_seg + "[##]" + abs_seg + "[##]" + claim_seg + "[##]" + des_seg

    return str


if __name__ == "__main__":

    input_path = sys.argv[1]
    out_path = sys.argv[2]
    # seg_dic = sys.argv[3]

    conf = SparkConf().setAppName("spark segment")
    sc = SparkContext.getOrCreate(conf=conf)

    # sc.addFile(seg_dic)

    rdd = sc.textFile(input_path).repartition(100).map(lambda line: line_format(line))
    rdd.saveAsTextFile(out_path)
    sc.stop()