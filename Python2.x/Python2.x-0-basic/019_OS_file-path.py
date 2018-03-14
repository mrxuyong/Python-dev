# -*- coding: UTF-8 -*-

# @author: xuyong

# @file: 019_OS_file-path.py

# @time: 2017/9/7 上午11:43

# @desc: OS 文件/目录方法

import os;


print os.access('myOS_file-path.txt', os.R_OK);
print os.access('myOS_file-path.txt', os.W_OK);
print os.access('myOS_file-path.txt', os.X_OK);


