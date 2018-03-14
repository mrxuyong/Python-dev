# -*- coding: UTF-8 -*-

# @author: xuyong

# @file: 105_http_2.py

# @time: 2017/9/15 下午4:37

# @desc: http 调用本地的 服务；

import httplib

BODY = "***filecontents***"
conn = httplib.HTTPConnection("localhost", 8080)
conn.request("GET", "/login", BODY)
resp = conn.getresponse()

# print response
print 'status:', resp.status, ', reason:', resp.reason
