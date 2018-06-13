#!usr/bin/python
# -*-coding:utf-8-*-
'''
2. 深刻理解Python中的元类（metaclass）
http://python.jobbole.com/21351/

Python中所有的东西，注意，我是指所有的东西——都是对象。这包括整数、字符串、函数以及类。它们全部都是对象，而且它们都是从一个类创建而来。
'''
import copy

a = [1, 2, 'c', ['de', 'ff']]
b = copy.copy(a)
a[3][0] = 'gg'
print b
