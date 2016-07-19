#!/usr/bin/pythona
import sys
import sys
import types
from operator import add
from pyspark import SparkContext
text_file="hdfs://xxx:8020/user/xxx/input/*"
#text_file="in.txt"
def myadd(x, y):
    return x + x

if __name__ == "__main__":
    sc = SparkContext(appName="PythonWordCount")
    print "helo"
    lines = sc.textFile(text_file)
    output = lines.collect()
    counts = lines.flatMap(lambda x : x.split(' ')) \
                 .map(lambda x : ( x , 1 ) )\
         .reduceByKey( myadd )
    output = counts.collect()
    print type(lines)
    print type(counts)
    print type(output)
    for ( word, count ) in output:
        if type(word) == types.UnicodeType:
            word = word.encode("utf-8")
        print "%s: %i"%(word, count)
