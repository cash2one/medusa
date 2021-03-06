#!/usr/bin/env python
# coding:utf-8

"""
descriptor
"""
"""
definition(short version):
    Descriptors are objects with any of __get__() , __set__() , or __delete__().
    These descriptor objects can be used as attributes on other class definitions.

definition:
    In general, a descriptor is an object attribute with "binding behavior",
    one whose attribute access has been overridden by methods in the descriptor protocol.
    Those methods are __get__(), __set__(), and __delete__().
    If any of those methods are defined for an object, it is said to be a descriptor.
"""
"""
What Are Descriptors?

    A descriptor is an object with any of the following methods (__get__() , __set__() , or __delete__() ),
    intended to be used via dotted-lookup as if it were a typical attribute of an instance.
    For an owner-object, [obj_instance], with a [descriptor] object:

        descriptor.__get__(self, obj_instance, owner_class) (returning a value)
            is invoked by
        obj_instance.descriptor

        descriptor.__set__(self, obj_instance, value) (returning None)
            is invoked by
        obj_instance.descriptor = value

        descriptor.__delete__(self, obj_instance) (returning None)
            is invoked by
        del obj_instance.descriptor

    obj_instance is the instance whose [class] contains the descriptor object's [instance].
    self is the [instance] of the descriptor (probably just one for the class of the obj_instance)
"""
"""
Descriptor Protocol
    descr.__get__(self, obj, type=None) --> value
    descr.__set__(self, obj, value) --> None
    descr.__delete__(self, obj) --> None

    That is all there is to it. Define any of these methods and an object is considered a descriptor
    and can override default behavior upon being looked up as an attribute.

    If an object defines both __get__() and __set__(), it is considered a [data descriptor] .
    Descriptors that only define __get__() are called [non-data descriptors] .
    (they are typically used for methods but other uses are possible).

    Data and non-data descriptors differ in how overrides are calculated with respect to entries in an instance’s dictionary.
    If an instance’s dictionary has an entry with the same name as a data descriptor, the data descriptor takes precedence.
    If an instance’s dictionary has an entry with the same name as a non-data descriptor, the dictionary entry takes precedence.

    To make a read-only data descriptor, define both __get__() and __set__() with the __set__() raising an AttributeError when called.
    Defining the __set__() method with an exception raising placeholder is enough to make it a data descriptor.
"""
print '-------------------------------------------------------------------------------------------------------'
"""
定义:
    descriptor 是实现了 __get__(), __set__(), __delete__() 方法的类的实例(对象)。
    任何实现 __get__(), __set__(), __delete__() 方法中一至多个的类的对象，都是 descriptor 对象。
"""
"""
一句话概括: 描述符就是可重用的属性。

property: 把函数调用伪装成对属性的访问。不足: 不能重复使用。
descriptor: 是property的升级版，允许为重复的property逻辑编写单独的类来处理。优点: 可以重复使用。
"""
print '-------------------------------------------------------------------------------------------------------'
class NonNegative(object):
    def __init__(self):
        """
        每个 NonNegative 的实例都维护着一个字典，其中保存着 [所有者实例] 和 [对应数据] 的映射关系。
        当我们访问 instance.attr 时，
            __get__ 方法会查找与 instance 相关联的数据，并返回这个结果。
        当我们执行 instance.attr = xxx 时，
            __set__ 方法采用的方式相同，只是这里会包含额外的非负检查。
        """
        self.dict = dict()
        pass

    def __get__(self, instance, owner):
        print '(descriptor get)(instance = %s)(owner = %s) %s' % (instance, owner, self.dict.get(instance))
        return self.dict.get(instance)

    def __set__(self, instance, value):
        print '(descriptor set)(instance = %s)(value = %s)' % (instance, value)
        if value < 0:
            raise ValueError('value can not be negative')
        self.dict[instance] = value

class Math(object):
    """
    NonNegative 实例
    是完全通过类属性模拟实例属性，
    因此实例属性其实根本不存在。
    """
    pid = NonNegative()  # descriptor 对象(Math的类属性)
    score = NonNegative()  # descriptor 对象(Math的类属性)

    def __init__(self, pid, score):
        """
        通过在 __init__() 内直接调用类属性,实现对实例属性初始化赋值的模拟.
        """
        """
        这里并未创建实例属性 pid 和 score, 而是调用类属性 Math.pid 和 Math.score
        """
        self.pid = pid
        self.score = score

    def check(self):
        if self.score >= 60:
            print 'PASS'
        else:
            print 'FAIL'

print '-------------------------------------------------------------------------------------------------------'
print Math.score
# (descriptor get)(instance = None)(owner = <class '__main__.Math'>) None
# None

print Math.pid
# (descriptor get)(instance = None)(owner = <class '__main__.Math'>) None
# None
print '-------------------------------------------------------------------------------------------------------'
s1 = Math(1, 90)
# (descriptor set)(instance = <__main__.Math object at 0x10f177c10>)(value = 1)
# (descriptor set)(instance = <__main__.Math object at 0x10f177c10>)(value = 90)

s1.score
# (descriptor get)(instance = <__main__.Math object at 0x10f177c10>)(owner = <class '__main__.Math'>) 90

s1.score = 61
# (descriptor set)(instance = <__main__.Math object at 0x10f177c10>)(value = 61)

s1.check()
# (descriptor get)(instance = <__main__.Math object at 0x10f177c10>)(owner = <class '__main__.Math'>) 61
# PASS

s1.score = 59
# (descriptor set)(instance = <__main__.Math object at 0x10f177c10>)(value = 59)

s1.check()
# (descriptor get)(instance = <__main__.Math object at 0x10f177c10>)(owner = <class '__main__.Math'>) 59
# FAIL
print '-------------------------------------------------------------------------------------------------------'
s2 = Math(2, 59)
# (descriptor set)(instance = <__main__.Math object at 0x10f177c50>)(value = 2)
# (descriptor set)(instance = <__main__.Math object at 0x10f177c50>)(value = 59)

s2.score = 50
# (descriptor set)(instance = <__main__.Math object at 0x10f177c50>)(value = 50)

s2.check()
# (descriptor get)(instance = <__main__.Math object at 0x10f177c50>)(owner = <class '__main__.Math'>) 50
# FAIL

s2.score = 99
# (descriptor set)(instance = <__main__.Math object at 0x10f177c50>)(value = 99)

s2.check()
# (descriptor get)(instance = <__main__.Math object at 0x10f177c50>)(owner = <class '__main__.Math'>) 99
# PASS
print '-------------------------------------------------------------------------------------------------------'
"""
描述符(descriptor)秘诀和陷阱
[1] 描述符需要放在类的层次上([descriptor实例]是[owner类]的[类属性])
[2] 确保实例的数据只属于实例本身,而不是所有的实例都共享相同的数据(这也是为什么我们要在NonNegative中使用数据字典的原因)
[3] 注意不可哈希的描述符所有者(NonNegative类使用了一个字典来单独保存专属于实例的数据。这个一般来说是没问题的，除非你用到了不可哈希的对象)
[4] 访问描述符的方法。描述符仅仅是类，所以可以为它们增加一些方法。(举个例子，描述符是一个用来回调property的很好的手段)
"""
