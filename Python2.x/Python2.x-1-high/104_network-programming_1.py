# -*- coding: UTF-8 -*-

# @author: xuyong

# @file: 104_network-programming_1.py

# @time: 2017/9/8 上午9:47

# @desc: Python 网络编程
# Python 提供了两个级别访问的网络服务。：
# 低级别的网络服务支持基本的 Socket，它提供了标准的 BSD Sockets API，可以访问底层操作系统Socket接口的全部方法。
# 高级别的网络服务模块 SocketServer， 它提供了服务器中心类，可以简化网络服务器的开发。

# 什么是 Socket?
# Socket又称"套接字"，应用程序通常通过"套接字"向网络发出请求或者应答网络请求，使主机间或者一台计算机上的进程间可以通讯。

# socket()函数
# Python 中，我们用 socket（）函数来创建套接字，语法格式如下：
# socket.socket([family[, type[, proto]]])
# 参数
# family: 套接字家族可以使AF_UNIX或者AF_INET
# type: 套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM
# protocol: 一般不填默认为0.


