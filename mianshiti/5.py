#!usr/bin/python
# ! -*- coding:utf-8 -*-
# 字典推导式
a = {}
a['19'] = 'zhaoying'
a['24'] = 'huwangwang'
for i in a:
    print i   #19 24
for i in a.values():
    print i   #zhaoying huwangwang
for i in a.keys():
    print i   #19 24
d = {key: value for (key, value) in a.items()}
print d
