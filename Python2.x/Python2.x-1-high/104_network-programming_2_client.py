# -*- coding: UTF-8 -*-

# @author: xuyong

# @file: 104_network-programming_2_client.py

# @time: 2017/9/8 上午10:00

# @desc: 客户端

import socket

s = socket.socket()
host = ''; # host = socket.gethostname()
port = 18110

s.connect((host, port))
print "server response info:", s.recv(100) #最多返回 100 个字符
s.close()
