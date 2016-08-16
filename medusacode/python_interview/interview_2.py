#!/usr/bin/env python
# coding:utf-8

print '----------------------------------------------------------------------------------------------------'
"""
def 指令
    Python 是动态语言，def 实际上是执行一条指令，用来创建函数，而不仅仅是个语法关键字。
    函数并不是事先创建好的，而是执行到的时候才创建的。
    def func() 将会创建一个名称为 func 的函数对象。

不要使用可变对象作为函数的默认参数例如 list，dict，
因为def是一个可执行语句，只有def执行的时候才会计算默认参数的值，
所以使用默认参数会造成函数执行的时候一直在使用同一个对象，引起bug。
"""
def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
print "list1 = %s" % list1, id(list1)
list2 = extendList(123, [])
print "list2 = %s" % list2, id(list2)
list3 = extendList('a')
print "list3 = %s" % list3, id(list3)
"""
list1 = [10] 4561453136
list2 = [123] 4561488496
list3 = [10, 'a'] 4561453136
"""
print '--------------------------------------------------'
def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')
print "list1 = %s" % list1, id(list1)
print "list2 = %s" % list2, id(list2)
print "list3 = %s" % list3, id(list3)
"""
list1 = [10, 'a'] 4365060576
list2 = [123] 4365060792
list3 = [10, 'a'] 4365060576
"""
print '----------------------------------------------------------------------------------------------------'
print '----------------------------------------------------------------------------------------------------'
print '----------------------------------------------------------------------------------------------------'
print '----------------------------------------------------------------------------------------------------'
print '----------------------------------------------------------------------------------------------------'
print '----------------------------------------------------------------------------------------------------'
print '----------------------------------------------------------------------------------------------------'





