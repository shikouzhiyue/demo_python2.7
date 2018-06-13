#!usr/bin/python
# ! -*- coding:utf-8 -*-
'''
6. Python中的单下划线和双下划綫
'''


class MyClass():
    def __init__(self):
        self.__superprivate = 'zhaoying'
        self._semiprivate = 'lizhihui'
mc = MyClass()
print mc._semiprivate      #lizhihui
#print mc.__superprivate    #报错
print mc.__dict__