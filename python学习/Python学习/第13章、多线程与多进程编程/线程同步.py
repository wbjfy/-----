# 线程同步
# 两中方式：join  和  互斥锁
# 1join
# 在start下一行加join即可
# 2互斥锁
# 概念：对共享数据进行锁定，保证多个线程访问共享数据不会出现数据错误问题，保证同一时刻只能有一个线程去操作
# 方法
# acquire():上锁
# release():释放锁
# 注意：这两个方法必须成对出现，否则容易形成死锁
# 死锁：一直等待对方释放锁的场景
# 死锁会造成应用程序停止响应，不再处理其他任务
import threading
from threading import Thread,Lock
import time

a = 0
b = 100000000#数字大才可以
lock = Lock()
def add():
    lock.acquire()   #上锁
    for i in range(b):
        global a
        a += 1
    print('第一次累加',a)
    lock.release()    #解锁

def add2():
    lock.acquire()
    for i in range(b):
        global a
        a += 1
    print('第二次累加',a)
    lock.release()
if __name__ == '__main__':
    first = threading.Thread(target=add)
    second = threading.Thread(target=add2)
    first.start()
    second.start()
#互斥所是多个线程一起去枪，抢到锁的线程先执行
