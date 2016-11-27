#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Author: zhihuazhang
# @File: singleton.py
# @Time: 16/11/28 上午1:28

def singleton(cls):
    # 单例模式
    instances = {}
    def _singleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton




if __name__ == '__main__':
    pass