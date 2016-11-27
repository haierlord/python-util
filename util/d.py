#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Author: zhihuazhang
# @File: d.py
# @Time: 16/11/24 上午1:03

import logging
import logging.config
import zh_logging

logger = zh_logging.Logger('log.log')
logger.info("asdf")


def test():
    # logging.config.fileConfig('./logging.conf')
    # root_logger = logging.getLogger('main')
    # root_logger.info("hahah")
    # root_logger.debug("asasd")
    logger = zh_logging.Logger('log.log')
    logger.info("asdf1")
    logger.info("asdasdff1")





if __name__ == '__main__':
    test()
    pass