# -*- coding: UTF-8 -*-

# 1.1 raw_input函数
# raw_input([prompt]) 函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）：

# str = raw_input("请输入: ");
# print "你输入的内容是: ", str;

# 1.2 input函数
# input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，但是 input 可以接收一个Python表达式作为输入，并将运算结果返回。

# str2 = input('请输入-->>');
# print '你输入的内容是-->>', str2;

# 2. 打开和关闭文件

# 2.1 open 函数

# 2.2 file 对象 的属性
# file.closed	返回true如果文件已被关闭，否则返回false。
# file.mode	返回被打开文件的访问模式。
# file.name	返回文件的名称。
# file.softspace	如果用print输出后，必须跟一个空格符，则返回false。否则返回true。

# 3. close()方法
# 4. write()方法
# 5. read()方法

# 6. 文件定位
# tell()方法告诉你文件内的当前位置；换句话说，下一次的读写会发生在文件开头这么多字节之后。
# seek（offset [,from]）方法改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置。
# 如果from被设为0，这意味着将文件的开头作为移动字节的参考位置。如果设为1，则使用当前的位置作为参考位置。如果它被设为2，那么该文件的末尾将作为参考位置。

# 打开一个文件
fo = open("myIO.txt", "r+")
tempStr = fo.read(20);
print "读取的字符串是 : ", tempStr

# 查找当前位置
position = fo.tell();
print "当前文件位置 : ", position

# 把指针再次重新定位到文件开头
position = fo.seek(0, 0);
tempStr = fo.read(20);
print "重新读取字符串 : ", tempStr
# 关闭打开的文件
fo.close()

# 7. 重命名和删除文件
import os

# 重命名文件 myIO.txt 到 myIO.txt。
# os.rename("myIO.txt", "myIO2.txt")

# 8. remove()方法
# os.remove('myIO2.txt')

# 9. python 里的目录

# 9.1 mkdir()方法
# os.mkdir("newdir")

# 9.2 chdir()方法:  用来改变当前的目录
# 将当前目录改为"/opt"
# os.chdir("/opt")

# 9.3 getcwd()方法：
# getcwd()方法显示当前的工作目录。
print os.getcwd();

# 9.4 rmdir()方法
# rmdir() 方法删除目录，目录名称以参数传递。
# 在删除这个目录之前，它的所有内容应该先被清除。


# 10. 文件、目录相关的方法
# 三个重要的方法来源能对Windows和Unix操作系统上的文件及目录进行一个广泛且实用的处理及操控，如下：
# File 对象方法: file对象提供了操作文件的一系列方法。
# OS 对象方法: 提供了处理文件及目录的一系列方法。
