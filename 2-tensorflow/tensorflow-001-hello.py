# -*- coding: UTF-8 -*-

# @author: xuyong

# @file: tensorflow-001-hello.py

# @time: 2018/1/9 下午6:31

# @desc:

import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
tf.enable_eager_execution()

result1 = tf.add(1, 2).numpy()
# print('result1:', result1)
# 3

# tf.constant("Hello,TensorFlow!").numpy()
hello = tf.constant("Hello,TensorFlow!")
hello.numpy()
# b'Hello,TensorFlow!' #前面多一个字母b是因为

# print('result2-hello:', hello)
# result2-hello: tf.Tensor(b'Hello,TensorFlow!', shape=(), dtype=string)

result3 = tf.constant(123).numpy()
# 123
