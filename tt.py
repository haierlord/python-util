#!/usr/bin/env python
# -*- coding: utf-8 -*-
# haierlord@gmail.com 2016-07-20 12:16:44
import requests

def tt15():
    a = [123,4]

    for i in range(10):
        try:
            print a[i]
        except Exception, e:
            print i
            raise e
            continue

class ShortInputException(Exception):
    '''你定义的异常类。'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

# try:
#     s = raw_input(u'请输入 --> ')
#     if len(s) < 3:
#         raise ShortInputException(len(s), 3)
#     # raise引发一个你定义的异常
# except EOFError:
#     print u'/n你输入了一个结束标记EOF'
# except ShortInputException, x:#x这个变量被绑定到了错误的实例
#     print u'ShortInputException: 输入的长度是 %d, 长度至少应是 %d' % (x.length, x.atleast)
# else:
#     print '没有异常发生.'

class BBB(object):
    def __init__(self):
        self.bb = 1

class Bird(BBB):
    def __init__(self):
        self.hungry = True
        super(Bird, self).__init__()
    def eat(self):
        if self.hungry:
            print "Auaaa..."
            self.hungry = False
        else:
            print "No, thanks"

class SongBird(Bird):
    def __init__(self):
        super(SongBird, self).__init__()
        self.sound = "saasas"
    def sing(self):
        print self.bb


class superDict(dict):
    def __init__(self):
        super(superDict, self).__init__()

    def hahaha(self):
        print "hhhhh"


class rec(object):

    def __init__(self):
        super(rec, self).__init__()
        self.width = 1
        self.heigh = 1
        # self.size = property(self.getSize, self.setSize)

    def getSize(self):
        return self.width, self.heigh

    def setSize(self, size):
        self.width, self.heigh = size

    size = property(getSize, setSize)

def getEle(item):
    # if isinstance(item, int):
    #     yield item
    # else:
    try:
        for t in item:
            print "***", t
            for t1 in getEle(t):
                yield t1, "+"
            # yield t
            # getEle(t)
    except:
        yield item, "-"


def test1():
    a = [[[1,2], [3,4]], 5]
    t = getEle(a)
    for k in t:
        print k


if __name__ == '__main__':

    test1()



    pass
