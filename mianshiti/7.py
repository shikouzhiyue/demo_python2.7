#!usr/bin/python
# ! -*- coding:utf-8 -*-
'''
7. *args and **kwargs
当你不确定你的函数里将要传递多少参数时你可以用*args.例如,它可以传递任意数量的参数:
*args和**kwargs可以同时在函数的定义中,但是*args必须在**kwargs前面.
'''


def print_everything(*args):
    for count, thing in enumerate(args):
        print '{0}, {1}'.format(count, thing)


print_everything('zhaoyinlg', 'liyujin', 'lizhihui')


def table_things(**kwargs):
    for name, value in kwargs.items():
        print '{0} = {1}'.format(name, value)


table_things(chuzhong='zhaoying', gaozhong='liyujin', gaozhong2='lizhihui')


def print_three_things(a, b, c):
    print 'a={0}, b={1}, c={2}'.format(a, b, c)


mylist = ['zhaoying', 'lizhihui', 'liyujin']
print_three_things(*mylist)   #注意此处是用的*mylist
