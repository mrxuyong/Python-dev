# -*- coding: UTF-8 -*-

# @author: xuyong

# @file: 104_network-programming_2_server.py

# @time: 2017/9/8 上午9:59

# @desc: 服务端

import socket  # 导入 socket 模块

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建 socket 对象
host = ''; # host = socket.gethostname()  # 获取本地主机名
port = 18110;  # 设置端口
s.bind((host, port))  # 绑定端口

s.listen(5)  # 等待客户端连接
while True:
    c, addr = s.accept()  # 建立客户端连接。
    print 'client request address:', addr
    c.send(''.join(['welcome visit ', str(port), ' server']))
    c.close()  # 关闭连接
