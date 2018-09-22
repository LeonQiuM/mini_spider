#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Leon"
# Date: 2018/9/22
import random
import time
import sys


class USAGE(object):
    def __init__(self):
        self.params = {
            'Region': 'gz',
            'Nonce': random.randint(1, sys.maxint),
            'Timestamp': int(time.time()),
        }
        self.files = {}
        self.host = 'cdn.api.qcloud.com'
        self.uri = '/v2/index.php'
        self.method = "GET"
        self.debug = 1


def main():
    pass


if __name__ == '__main__':
    sys.exit(main())
