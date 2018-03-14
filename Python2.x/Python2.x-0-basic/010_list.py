# -*- coding: UTF-8 -*-
# Python有6个序列的内置类型，但最常见的是列表和元组。
# http://www.runoob.com/python/python-lists.html

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7];

print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]

print;
print '遍历 list1 --start--';
for x in list1:
    print x;
print '遍历 list1 --end--';
print;

del list1[2];
print "After deleting value at index 2 : "
print list1;

print list2[-2];
print 'list2 length:', len(list2);
