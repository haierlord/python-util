#!/usr/bin/env python
# -*- coding: utf-8 -*-
# haierlord@gmail.com 2016-09-21 23:02:29

def test():
    hotels = {1: ("H1", "T"), 2: ("H2", "T"), 3: ("H3", "F"), 4: ("H4", "T"), 5: ("H5", "T"), 6: ("H6", "F")}
    # 5 --> 2
    start, end = 1, 5
    head = start
    tempPair = [-1, hotels[end]]
    while start != end:
        if hotels[start][1] == "T" and head != start and (tempPair[1][1] != "T"):
            start += 1
            continue
        curPair = [start, hotels[start]]
        hotels[start] = tempPair[1]
        tempPair = curPair
        start += 1
    hotels[end] = tempPair[1]
    print hotels



if __name__ == '__main__':
    test()
    pass
