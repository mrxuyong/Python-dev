# -*- coding: UTF-8 -*-
# pass是空语句，是为了保持程序结构的完整性。
# pass 不做任何事情，一般用做占位语句。

# 输出 Python 的每个字母
for letter in 'Python':
    if letter == 'h':
        pass
        print '这是 pass 块'
    print '当前字母 :', letter

print "Good bye!"


# 当你在编写一个程序时，执行语句部分思路还没有完成，这时你可以用pass语句来占位，也可以当做是一个标记，是要过后来完成的代码。比如下面这样：
def playPython():
    pass
