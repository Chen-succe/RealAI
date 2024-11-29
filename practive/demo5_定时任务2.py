import sched
import time
import datetime
import signal
# import apscheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import hashlib

def img_to_md5(_path):
    fd = open(_path, 'rb')
    fmd5 = hashlib.md5(fd.read()).hexdigest()
    fd.close()
    return fmd5
def a():
        print(datetime.datetime.now())
        global dict_a
        dict_a = {}
        print(dict)

def task_same_md5(im=0):
    md5 = img_to_md5(im)
    print(md5, type(md5))
    dict_a[md5] = datetime.datetime.now()
    print(dict)
    
    
    
if __name__ == '__main__':
    sc = BackgroundSchsceduler()
    # cron 触发器中其中一种触发类型，在特定时间周期性地触发
    sc.add_job(a, 'cron', hour=17, minute=35)
    # sc.add_job(a, 'interval', seconds=3)
    sc.start()
    # ctrl+c 停止
    # signal.signal(signal.SIGINT, signal.SIG_DFL)
    dict_a = {}
    task_same_md5('E:\\train_data\\train_class\\train_class\\9\\48582.jpg')
    # try:
    #     while True:
    #         time.sleep(2)
    #         print(dict_a)
    # except(KeyboardInterrupt, SystemExit):
    #     sc.shutdown()
    
    
    
