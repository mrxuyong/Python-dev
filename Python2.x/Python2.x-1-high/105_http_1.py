# -*- coding: UTF-8 -*-

# @author: xuyong

# @file: 105_http_1.py.py

# @time: 2017/9/15 上午11:34

# @desc: http 使用 head, body 方法的示例会话；

import httplib, urllib

params = urllib.urlencode({'@duserCode': 'D00017'})
headers = {"Content-type": "application/json;charset=UTF-8", "Accept": "*/*"}
body = "***filecontents***"

conn = httplib.HTTPConnection("www.baidu.com")

# print conn
# conn.request("GET", "/", params, headers)
# conn.request("GET", "/", body, headers)
# conn.request("GET", "/", "", headers)
conn.request("GET", "/")

resp = conn.getresponse()
# print response
print 'status:', resp.status, ', reason:', resp.reason
