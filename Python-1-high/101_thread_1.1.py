# Python use thread have two ways: function or in class new thread object

# 1. function way : use thread module start_new_thread() create new thread. eg:
# thread.start_new_thread ( function, args[, kwargs] )


# !/usr/bin/python
# -*- coding: UTF-8 -*-

import thread
import time


# define a thread function
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % (threadName, time.ctime(time.time()))


# create two thread
try:
    thread.start_new_thread(print_time, ("Thread-1", 2,))
    thread.start_new_thread(print_time, ("Thread-2", 4,))
except:
    print "Error: unable to start thread"

while 1:
    pass
