# _*_　coding=utf-8 _*_
import time
ticks=time.time()
print "当前时间戳为：",ticks
print time.localtime()
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
import datetime
print datetime.datetime.now()