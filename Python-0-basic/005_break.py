# -*- coding: UTF-8 -*-

# 第一个实例
for letter in 'Python':
    if letter == 'h':
        break;
    print '当期字母 :', letter

# 第二个实例
var = 10
while var > 0:
    print '当期变量值 :', var
    var = var - 1
    if var == 5:  # 当变量 var 等于 5 时退出循环
        break;

print "Good bye!"
