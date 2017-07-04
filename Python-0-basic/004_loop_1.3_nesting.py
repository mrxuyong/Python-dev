# -*- coding: UTF-8 -*-

print '----****---- 1.3.1 start ----****----';
tempArray = [];
i = 2
while (i < 100):
    j = 2
    while (j <= (i / j)):
        if not (i % j): break
        j = j + 1
    if (j > i / j): tempArray.append(i);  # print i, " 是素数"

    i = i + 1

# print ('-->>', tempArray)
print '素数-->>', tempArray
print '----****---- 1.3.1 end ----****----';
print;

print '----****---- 1.3.2 start ----****----';
num = [];
i = 2
for i in range(2, 100):
    j = 2
    for j in range(2, i):
        if (i % j == 0):
            break
    else:
        num.append(i)

# print('-->>', num);
print '素数-->>', num;
print '----****---- 1.3.2 end ----****----';
print;

print '----****---- 1.3.3 start ----****----';

# *字塔
i = 1
# j=1
while i <= 9:
    if i <= 5:
        print ("*" * i)

    elif i <= 9:
        j = i - 2 * (i - 5)
        print("*" * j)
    i += 1
else:
    print("");

print '----****---- 1.3.3 end ----****----';
