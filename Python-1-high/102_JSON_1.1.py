# -*- coding: UTF-8 -*-

# 使用 Python 语言来编码和解码 JSON 对象
# 使用 JSON 函数需要导入 json 库：import json

# json.dumps	将 Python 对象编码成 JSON 字符串
# json.loads	将已编码的 JSON 字符串解码为 Python 对象

import json;

data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}];
json = json.dumps(data);
print 'json:', json;
print 'type(data):', type(data);
print 'type(json):', type(json);

data1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5};
print 'type(data1):', type(data1);
