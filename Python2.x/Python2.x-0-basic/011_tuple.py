# -*- coding: UTF-8 -*-

# Python的元组与列表类似，不同之处在于元组的元素不能修改。
# 1. 元组使用小括号，列表使用方括号。
# 2. 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"

tup4 = ()
tup5 = (50,)

print '遍历元组 --start--'
for i in tup1:
    print i
print '遍历元组 --end--\n'

tup6 = ('python1', 'python2')
tup7 = ('python1', 'python3')
print cmp(tup6, tup7)

# 将元组转换为列表
print '将元组转换为列表-->>', list(tup1)
