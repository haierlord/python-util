#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Author: zhihuazhang
# @File: updateDict.py
# @Time: 16/11/23 下午11:53


def updateDict(dict_, key, value = 1):
    try:
        hash(key)
        if key not in dict_:
            dict_[key] = 0
        dict_[key] += value
    except TypeError:
        for k in key:
            if k not in dict_:
                dict_[k] = 0
            dict_[k] += value





if __name__ == '__main__':
    dict_ = {}
    updateDict(dict_, [1,4], 2)
    print dict_
    pass