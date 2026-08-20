from itertools import groupby
words=["apple","banana","cherry","date","elderberry","fig","cucumber"]
groups=groupby(sorted(words),key=lambda x:x[0])
for key,group in groups:
    print(key,list(group))