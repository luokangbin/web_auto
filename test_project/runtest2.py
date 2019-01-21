#coding=utf-8
__author__ = 'Administrator'
import unittest

from test_case import test_baidu, test_youdao


test_dir="./test_case/"
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__=="__main__":
    runner=unittest.TextTestRunner()
    runner.run(discover)
