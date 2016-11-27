#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Author: zhihuazhang
# @File: zh_logging.py
# @Time: 16/11/24 上午1:00

import logging
from singleton import singleton


@singleton
class Logger(object):
    def __init__(self, path, clevel=logging.DEBUG, Flevel=logging.DEBUG):
        # NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] (%(funcName)s-%(lineno)s) %(message)s',
                                '%Y-%m-%d %H:%M:%S')
        # 设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(clevel)
        # 设置文件日志
        fh = logging.FileHandler(path)
        fh.setFormatter(fmt)
        fh.setLevel(Flevel)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

        self.debug = self.logger.debug
        self.info = self.logger.info
        self.warn = self.logger.warn
        self.error = self.logger.error
        self.critical = self.logger.critical

    def setFileHandler(self, path = 'log.log', flevel = logging.DEBUG):
        fh = logging.FileHandler(path)
        fh.setLevel(flevel)
        self.logger.addHandler(fh)


    def set_format(self, fmt):
        self.logger.setFormatter(fmt)


def test():
    logger = Logger('log.log', logging.DEBUG, logging.DEBUG)

    logger.debug("as")
    logger.info("hashashasdhfh")
    # logger.logger.cri('asd')




class Zh_logging(object):
    def __init__(self, level = logging.INFO, name = None):
        # logging.basicConfig(level=level)
        logging.basicConfig(level=logging.INFO, format='%(asctime)-15s - %(funcName)s -- %(message)s--- %(lineno)d')
        self.logger = logging.getLogger(name)

    def setLevel(self, level):
        logging.basicConfig(level=level)

    def setFormat(self, formatter):
        logging.Formatter(formatter)

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
#
# logger.info("hello")
# logger.debug("debughere")
# logging.basicConfig(level=logging.DEBUG)






if __name__ == '__main__':
    test()
    pass