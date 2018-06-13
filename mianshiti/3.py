#!usr/bin/python
# ! -*- coding:utf-8 -*-
'''
@staticmethod 和 @classmethod
Python其实有3个方法,即静态方法(staticmethod),类方法(classmethod)和实例方法
\	     实例方法	          类方法	        静态方法
a = A()	a.foo(x)	a.class_foo(x)	a.static_foo(x)
A	     不可用	    A.class_foo(x)	A.static_foo(x)
'''


def foo(x):
    print "executing foo(%s)" % (x)


class A(object):
    def foo(self, x):
        print "executing foo(%s,%s)" % (self, x)

    @classmethod
    def class_foo(cls, x):
        print "executing class_foo(%s,%s)" % (cls, x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)" % x


a = A()
a.static_foo('s')
A.static_foo('s')
