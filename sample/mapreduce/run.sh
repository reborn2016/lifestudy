hadoop fs -rm -r /usr/xx/output
hadoop jar *hadoop-mapreduce-client/hadoop-streaming.jar  \
    -file mapper.py    -mapper ./mapper.py \
    -file reducer.py   -reducer ./reducer.py \
    -input /user/xx/input/data -output /user/xx/output
