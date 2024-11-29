import logging
import os

logger = logging.getLogger(__name__)

def do_something():
    logger.info("do something")

def main():
    logging.basicConfig(#filename='./a.log', 
                        level=logging.INFO,
                        format='[%(asctime)s] - %(message)s',
            datefmt='%Y/%m/%d %H:%M:%S',
                        handlers=[
                logging.FileHandler('a.log'),
                logging.StreamHandler()
                # StreamHandler实例会将消息发送到数据流（类似于文件对象）。
                # FileHandler实例会将消息写入磁盘文件
            ])
    # 通过使用默认的 Formatter 创建一个 StreamHandler 并将其加入根日志记录器来为日志记录系统执行基本配置
    # [注解]: 此函数应当在其他线程启动之前从主线程被调用。 在 2.7.1 和 3.2 之前的 Python 版本中，如果此函数从
    # 多个线程被调用，一个处理器（在极少的情况下）有可能被多次加入根日志记录器，导致非预期的结果例如日志中的
    # 消息出现重复。
    do_something()
    print(1+1)
    logger.info('Finished')
    
if __name__ == "__main__":
    main()
    # print(os.path.abspath(__file__))
