# -*- coding: UTF-8 -*-

# @author: xuyong

# @file: 202-fbnqsl.py

# @time: 2018/7/27 下午7:33

# @desc: 斐波那契数列实现

# 获取用户输入数据  # 随便手动输入数字，比如 10
# nterms = int(input("你需要几项？"))
nterms = 10

# 第一和第二项
n1 = 0
n2 = 1
count = 2

# 判断输入的值是否合法
if nterms <= 0:
    print("请输入一个正整数。")
elif nterms == 1:
    print("斐波那契数列：")
    print(n1)
else:
    print("斐波那契数列：")
    print(n1, ",", n2, end=", ")
    while count < nterms:
        nth = n1 + n2
        print(nth, end=", ")
        # 更新值
        n1 = n2
        n2 = nth
        count += 1
