# -*- coding: UTF-8 -*-

# @author: xuyong

# @file: 102_JSON_1.2_demJson.py.py

# @time: 2017/9/7 下午3:58

# @desc: 第三方库：Demjson

# 先下砸，后安装，最后使用；
# tar -xvzf demjson-2.2.3.tar.gz
# cd demjson-2.2.3
# python setup.py install

import demjson

tempData = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]

json = demjson.encode(tempData)
print "json:", json

tempJsonStr = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

data = demjson.decode(tempJsonStr)
print "data:", data
