import datetime
import time

# time
'''time 模块是围绕着 Unix Timestamp 进行的,所以其所能表述的日期范围被限定在 
1970 - 2038 之间，如果你写的代码需要处理在前面所述范围之外的日期，那可能需要考虑使用datetime模块更好'''

time1 = time.time()
time.sleep(4)
time2 = time.time()
print(time.gmtime(time2))
print(time2-time1)
print(time.asctime(time.localtime(time.time())))

# datatime
'''datetime 比 time 高级了不少，可以理解为 datetime 基于 time 进行了封装，
提供了更多实用的函数。在datetime 模块中包含了几个类，具体关系如下:

object
    timedelta     # 主要用于计算时间跨度
    tzinfo        # 时区相关
    time          # 只关注时间
    date          # 只关注日期
        datetime  # 同时有时间和日期
        
在实际实用中，用得比较多的是 datetime.datetime 和 datetime.timedelta ，
另外两个 datetime.date 和 datetime.time 实际使用和 datetime.datetime 并无太大差别.

'''
print(datetime.datetime.now())

# datetime.timedelta 用来处理时间间隔
time1 = datetime.datetime.now()
time.sleep(4)
print(datetime.datetime.now() - time1)
delta = datetime.timedelta(hours=14)
print(datetime.datetime.now() + delta)