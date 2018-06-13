#!usr/bin/python
#! -*- coding:utf-8 -*-
"""
1. Python的函数参数传递
在python中，strings, tuples, 和numbers是不可更改的对象，而list,dict等则是可以修改的对象。(这就是这个问题的重点)
http://python.jobbole.com/85231/
"""
# a = 1
#
# def fun(a):
#     a = 2
# fun(a)
# print a #1

a= []
def fun(a):
    a.append(1)
fun(a)
print a #[1]