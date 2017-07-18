# -*- coding: UTF-8 -*-
# function

# 1.
# 定义一个函数
# 你可以定义一个由自己想要功能的函数，以下是简单的规则：
# 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
# 任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
# 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
# 函数内容以冒号起始，并且缩进。
# return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None

def myPrint(params):
    print 'this is ', params, '\n';

    return 'this is ', params;


myPrint('first function...')


# **** START **** #
# python 参数传递 规则：
# 在 python 中，类型属于对象，变量是没有类型的：
# 可更改(mutable)与不可更改(immutable)对象

# python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
# 不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
# 可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

# python 函数的参数传递：
# 不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
# 可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响

# python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。

# 2.1 python 传不可变对象实例
def changeInt(a):
    print 'a-- 1-->>', a;
    a = 10;
    print 'a-- 2-->>', a;


b = 2;

changeInt(b);
print 'b-->>', b, '\n';


# 2.2 传可变对象实例
def changeMe(myList):
    myList.append([1, 2, 3]);
    print '函数内取值: ', myList;
    return;


myList = [10, 20, 30];
changeMe(myList);
print '函数外取值: ', myList;


# **** END **** #


# 3. 参数 (必备参数, 关键字参数, 默认参数, 不定长参数)

# 3.1 必备参数(必须传入一个参数，不然会出现语法错误)
def printMe31(str):
    print str;  # "打印任何传入的字符串"
    return;


# printMe31();  # 调用printMe31函数


# 3.2 关键字参数(关键字参数顺序不重要)
def printMe32(name, age):
    print "Name:", name, ", Age:", age;  # "打印任何传入的字符串"
    return;


printMe32(age=50, name="miki");  # 调用 printMe32 函数


# 3.3 默认参数(缺省参数的值如果没有传入，则被认为是默认值)
def printMe33(name, age=24):
    print "Name:", name, ", Age:", age;  # "打印任何传入的字符串"
    return;


printMe33(age=50, name="Jack");
printMe33(name="Jack");


# 3.4 不定长参数(你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名。)
def printMe34(arg1, *vartuple):
    print '输出：'
    print arg1;

    for var in vartuple:
        print 'var-->>', var;
    return;


printMe34(10);
printMe34(50, 60, 70, 80);

# 4. 匿名函数
# python 使用 lambda 来创建匿名函数。
# lambda只是一个表达式，函数体比def简单很多。
# lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
# lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
# 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

print '\n匿名函数-->>';
# 4.1
mySum = lambda arg1, arg2: arg1 + arg2;

print '-->>', mySum(10, 20);
print '-->>', mySum(40, 40);


# 5. return 语句
def mySum5(arg1, arg2):
    total = arg1 + arg2;
    print '函数内输出:', total;
    return total;


total = mySum5(10, 20);

# 6. 变量作用域(全局变量 和 局部变量)
