# -*- coding: UTF-8 -*-

# @author: xuyong

# @file: 103_CGI_1.1.py

# @time: 2017/9/7 下午4:08

# @desc: CGI(Common Gateway Interface),通用网关接口,它是一段程序,运行在服务器上如：HTTP服务器，提供同客户端HTML页面的接口。

print "Content-type:text/html"
print  # 空行，告诉服务器结束头部
print '<html>'
print '<head>'
print '<meta charset="utf-8">'
print '<title>Hello Word - 我的第一个 CGI 程序！</title>'
print '</head>'
print '<body>'
print '<h2>Hello Word!</h2>'
print '</body>'
print '</html>'
