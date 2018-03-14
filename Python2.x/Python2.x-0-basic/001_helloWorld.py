# -*- coding: UTF-8 -*-

import os, sys

print "this is 001_helloWorld.py ...."

print '__doc__:', __doc__, '\n';
print '__file__:', __file__, '\n';  # 特殊字符串变量 __file__ 指向该模块的导入文件名;
print '__name__:', __name__, '\n';  # 特殊字符串变量 __name__ 指向模块的名字;

print 'os.getcwd():', os.getcwd(), '\n';
print 'os.path.realpath(__file__):', os.path.realpath(__file__), '\n';

print 'sys.path[0]:', sys.path[0], '\n';
print 'sys.argv[0]:', sys.argv[0], '\n';
