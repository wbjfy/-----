# 多任务
import time
def sing():
    print('我在唱歌')
    time.sleep(2)    #睡眠，以秒为单位
    print('唱完歌了')
def dance():
    print('在跳舞')
    time.sleep(2)
    print('跳完舞了')
sing()
dance()

# 多线程：同时运行多个线程
# 线程
# 含义：是cpu调度的基本单位，每一个进程至少都会有一个线程，这个线程通常是我们所说的主线程
# 进程：是操作系统进行资源分配的基本单位，每打开一个程序至少就会有一个进程
# 一个进程默认有一个线程，进程里面可以创建多个线程，线程是依附在进程里面的，没有进程就没有线程
# 导入线程模块
# import threading
# Thread线程类参数
# target：执行的任务名
# args：以元组的形式给任务传参
# kwargs：以字典的形式给任务传参
# 模块函数看书271页
import threading
import time
def sing(name):
    print(f'{name}1234')
    time.sleep(2)
    print('5678')
def dance(name2):
    print(f'{name2}abcd')
    time.sleep(2)
    print('efgh')
#主程序入口
if __name__ == '__main__':
    #1创建子线程
    t1 = threading.Thread(target=sing,args=('bingbing',)) #以元组的形式传参只有一个时要加逗号
    # print(t1)
    t2 = threading.Thread(target=dance,args=('bingbing',))
    #3守护线程，必须放在start()前面
    t1.daemon = True
    t2.daemon = True
    #2开启子线程
    t1.start()
    t2.start()
    #4阻塞主线程join():暂停的作用，等子线程执行结束后，主线程才会继续执行，必须放在start()后面
    t1.join()
    t2.join()
    #5获取线程名字
    print(t1.name)
    print(t2.name)
    #更改线程名
    t1.name = ('子线程一')
    t2.name = ('子线程二')
    print(t1.name)
    print(t2.name)
    print('完美谢幕')


# 线程之间执行是无序的
# 线程执行时根据cpu调度决定的
import threading
import time
def task():
    time.sleep(1)
    print('当前线程是:',threading.current_thread().name)   #显示当前线程对象名
if __name__ == '__main__':
    for i in range(5):
        #每循环一次就创建一个子线程
        t = threading.Thread(target=task)
        #启动子线程
        t.start()

# 线程之间共享资源
import threading
import time

li = []   #定义全局变量
#写入数据
def wdata():
    for i in range(5):
        li.append(i)
        time.sleep(1)
    print('写入的数据是:',li)
#读取数据
def rdata():
    print('读取的数据是:',li)
if __name__ == '__main__':
    #创建子线程
    wd = threading.Thread(target=wdata)
    rd = threading.Thread(target=rdata)
    #开启子线程
    wd.start()
    wd.join()
    rd.start()
    rd.join()

# 资源竞争
import threading
import time

a = 0
b = 100000000     #数字大才可以
def add():
    for i in range(b):
        global a
        a += 1
    print('第一次累加',a)

def add2():
    for i in range(b):
        global a
        a += 1
    print('第二次累加',a)
if __name__ == '__main__':
    first = threading.Thread(target=add)
    second = threading.Thread(target=add2)
    first.start()
    second.start()
