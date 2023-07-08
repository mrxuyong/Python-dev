# -*- coding: UTF-8 -*-

# @author: xuyong

# @file: tools-001.py

# @time: 2023/7/8 15:52

# @desc:文件批量 重命名

import os

path = input('请输入文件路径(结尾加上/)：')  # /Volumes/XCJLY64G/2023-南洋女儿情/

# 获取该目录下所有文件，存入列表中
f = os.listdir(path)

n = 0
for i in f:
    print("f" + n, "====>>", f[n]);  # 南洋女儿情第35集.mp4 。。。

    # 旧文件名（就是路径+文件名）
    oldName = path + f[n]

    # 设置新文件名，[某个文字替换|添加某个字符 等等]
    newName = path + f[n].replace("第", '-')

    print(oldName, '====>>', newName)
    # 用os模块中的rename方法对文件改名
    # os.rename(oldName, newName)
    n += 1


print('====成功====')
