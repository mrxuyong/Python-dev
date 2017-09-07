# -*- coding: UTF-8 -*-
# python提供了两个非常重要的功能来处理python程序在运行中出现的异常和错误。你可以使用该功能来调试python程序。
# 1.异常处理;
# 2.断言(Assertions)。

# 一、 try...except...
try:
    fh = open('myException.txt', 'w')
    fh.write("this is test exception.")
except:
    print "Error: 没有找到文件或读取文件失败"
else:
    print "内容写入成功"
    fh.close()


# 在执行代码前为了测试方便，我们可以先去掉 testfile 文件的写权限，命令: chmod -w myException.txt

# 二、 触发异常 raise [Exception [, args [, traceback]]]
# 定义函数
def mye(level):
    if level < 1:
        raise Exception("Invalid level!", level)
        # 触发异常后，后面的代码就不会再执行


try:
    mye(0)  # // 触发异常
except "Invalid level!":
    print 1
else:
    print 2


# 三、 自定义异常

class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg


try:
    raise Networkerror("Bad hostname")
except Networkerror, e:
    print e.args
