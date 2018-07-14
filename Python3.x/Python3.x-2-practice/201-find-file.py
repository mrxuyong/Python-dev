# -*- coding: UTF-8 -*-

# @author: xuyong

# @file: 201-find-file.py

# @time: 2018/7/13 上午10:51

# @desc: 根据文件名称精确查找 某个文件；

# 方法一、 查找某个目录下的目标文件

import os  # 引入操作系统模块
import sys  # 用于标准输入输出


def search(filePath, fileName):
    # print ('filePath--0:', filePath, ', fileName--0', fileName, ', os.walk(filePath):', os.walk(filePath))
    for root, dirs, files in os.walk(filePath):  # filePath 为根目录
    # for root, dirs, files in os.walk('/'):
    # for root, dirs, files in os.walk('/share'):
    #     print ('root:', root, ', dirs:', dirs, ', files:', files)
        if fileName in dirs or fileName in files:
            flag = 1  # 判断是否找到文件
            root = str(root)
            dirs = str(dirs)
            files = str(files)
            # return os.path.join(root, dirs)
            # return os.path.join(root, dirs, files)
            return os.path.join(root, files)
    return -1


# filePath = input('请您输入要查找哪个目录的文件(eg:/opt)')
# # print ('filePath:', filePath)

print('请您输入要查找的文件名:')
fileName = sys.stdin.readline().rstrip()  # 标准输入，其中rstrip()函数把字符串结尾的空白和回车删除
# print ('fileName:', sys.stdin.readline())

filePath = '/share'
# fileName = 'test2.js'

answer = search(filePath, fileName)
if answer == -1:
    print("查无此文件")
else:
    print("had find-- answer:", answer)
