# -*- coding: UTF-8 -*-
# date time

import time;

ticks = time.time();
print 'timeStamp(Millisecond) is -->>', ticks;
print;

localTime = time.localtime(time.time());
print 'localTime is -->>', localTime;
print;

formatDateTime = time.asctime(time.localtime(time.time()));
print 'formatDateTime is -->>', formatDateTime;
print;
