# !/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Description: 
#
# @Time: 2021/9/22 10:47
import logging

logger = logging.getLogger()


def set_logger():
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(process)d-%(threadName)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


set_logger()
