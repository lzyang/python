#!/bin/bash

input_path="/data/caip/lzy/source/patent100w/"
out_path="/data/caip/lzy/source/patent100w_seg/"

hdfs dfs -rmr ${out_path}

#  --master spark://caip184:7077 \

#  --master yarn \
#  --deploy-mode cluster \

/data/caip/spark/spark-2.2.0-bin-hadoop2.7/bin/spark-submit \
  --master spark://caip184:7077 \
	--driver-memory 4g \
	--executor-memory 8g \
	--executor-cores 2 \
	--total-executor-cores 20 \
	--conf spark.default.parallelism=180 \
	--conf spark.executor.heartbeatInterval=36000 \
	--conf spark.worker.timeout=240000 \
	spark_seg.py ${input_path} ${out_path}