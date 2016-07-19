#!/usr/bin/python
import sys

current_count = 0
current_word = None
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except:
        continue
    if current_word == word:
        current_count += 1
    else:
        if current_word:
            print "%s\t%s"%(current_word, current_count)
        current_word = word
        current_count = count
if current_word == word:
    print "%s\t%s"%(current_word, current_count)
