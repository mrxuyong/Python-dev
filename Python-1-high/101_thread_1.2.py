# 2. use Threading module create thread
# use Threading module create thread, from threading.Thread extend, then overwrite __init__ Method and run Method:


# !/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time

exitFlag = 0


class myThread(threading.Thread):  # extend father threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):  # need running code write in run function, after create thread running run function
        print "Starting " + self.name
        print_time(self.name, self.counter, 5)
        print "Exiting " + self.name


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            thread.exit()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1


# create new thread
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# start thread
thread1.start()
thread2.start()

print "Exiting Main Thread"
