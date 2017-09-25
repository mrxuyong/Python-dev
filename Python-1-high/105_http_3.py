# -*- coding: UTF-8 -*-

# @author: xuyong

# @file: 105_http_3.py

# @time: 2017/9/25 上午9:42

# @desc: http 调用公网的 服务；

import httplib

BODY = "***filecontents***"

# conn = httplib.HTTPConnection("cwx-test.jz.qianmi.com")
# # conn.request("GET", "/D1234#/login", BODY)  # resp.status 404
# conn.request("GET", "/login", BODY)  # resp.status 200

conn = httplib.HTTPConnection("jz.bm001.com")
# conn.request("GET", "/custom/share")  # resp.status 400
# conn.request("GET", "/login")  # resp.status 302
conn.request("GET", "/")  # resp.status 200

# conn = httplib.HTTPConnection("www.python.org")
# # conn.request("GET", "/doc")  # resp.status 301
# # conn.request("GET", "/index.html")  # resp.status 301
# conn.request("GET", "/")  # resp.status 301

# conn = httplib.HTTPConnection("www.baidu.com")
# conn.request("GET", "/index.html", BODY)  # ; resp.status 200

resp = conn.getresponse()
print 'status:', resp.status, ', reason:', resp.reason
# print type(resp)
# print id(resp)
