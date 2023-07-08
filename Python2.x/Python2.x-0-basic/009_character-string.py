# -*- coding: UTF-8 -*-

# 字符串是 Python 中最常用的数据类型。我们可以使用引号('或")来创建字符串。

var1 = 'Hello World!'
var2 = 'Python Runoob - 001'

print("var1[0]: ", var1[0])
print("var2[0:6]: ", var2[0:6])

print("更新字符串 :- ", var1[:6] + 'Runoob!')

print(var2.split('-'))

# test replace 方法
# /Volumes/XCJLY64G/2023-南洋女儿情/
tempStr = "南洋女儿情第1集"
print("截取拼接字符====>>", tempStr[:5] + "-" + tempStr[6:])
print("截取替换====>>", tempStr.replace("第", '-'))
