# -*- coding: UTF-8 -*-
# module

# 1. 使用 import 语句来引入模块;
import myPrint;

myPrint.myPrint1('This is 015_module, using python module...');
print '入参为空时，打印默认的-->>\n'
myPrint.myPrint1();

# 2. From…import 从模块中导入一个指定的部分到当前命名空间中;

from myPrint import myPrint2;

myPrint2('from...import');

# 3. from...import* 把一个模块的所有内容全都导入到当前的命名空间;#

from myPrint import *

myPrint3('from...import*');
