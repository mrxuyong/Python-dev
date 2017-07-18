# -*- coding: UTF-8 -*-

# 搜索某个 路径下有多少 .js 类型的文件；

import os

# print os
print('cur file name-->>', __file__);
print('cur file path-->>', os.path.realpath(__file__))  # 当前文件的路径
print('cur file catalog-->>', os.path.dirname(os.path.realpath(__file__)))  # 从当前文件路径中获取目录
print('cur file name-->>', os.path.basename(os.path.realpath(__file__)))  # 从当前文件路径中获取文件名

# dirname = __file__
# print(os.listdir(dirname))  # 只显示该目录下的文件名和目录名，不包含子目录中的文件，默认为当前文件所在目录

sourcePath = '';
