# 进程
# 含义：是操作系统进行资源分配和调度的基本单位，是操作系统结构的基础
# 一个正在运行的程序或者软件就是一个进程
# 程序跑起来就成了进程
# 注意：进程里面可以创建多个线程，多进程也可以完成多个任务
# 进程的状态
# 1就绪状态：运行的条件都已经满足，正在等待cpu执行
# 2执行状态：cpu正在执行其功能
# 3等待(阻塞)状态：等待某些条件满足，如一个程序sleep了，此时就处于等待状态
import time
print('123456')     #程序处于执行状态
sex = input('请输入：')     #光标闪动，等待用户输入，处于等待状态
print(sex)    #执行状态
time.sleep(1)    #延时一秒，等待状态

# 进程语法结构
# multiprocessing模块提供了Process类代表进程对象
# Process类参数
# 1target：执行的目标任务名，即子进程要执行的任务
# 2args：以元组的形式传参
# 3kwargs：以字典的形式传参
# 方法
# 1start()：开启子进程
# 2is_alive():判断子进程是否还活着，存活返回True，死亡返回False
# 3join()：主进程等待子进程执行结束
from multiprocessing import Process

def eat(name):
    print(f'{name}吃饭')
def sleep(name):
    print(f'{name}睡觉')
if __name__ == '__main__':
    p1 = Process(target=eat,args=('bingbing',))
    p2 = Process(target=sleep,args=('bingbing',))
    p1.start()
    p1.join()   #主进程处于等待状态，p1是运行状态
    p2.start()
    print(p1.is_alive())
    print(p2.is_alive())
#写在主程序中判断存活状态时候需要加入join阻塞一下
#
# 常用的属性
# name：当前进程的别名。默认Process-N
# pid：当前进程的进程编号
import time
from multiprocessing import Process
import os
def sing():
    #so.getpid():获取当前进程编号
    #os.getppid():获取父进程编号
    print(os.getppid())    #父进程的pid就是py文件主进程的id
    print('唱歌')
def dance():
    print(os.getppid())
    print('跳舞')
if __name__ == '__main__':
    #创建子进程
    #修改子进程名的第一种方式
    p1= Process(target=sing,name = '1')
    p2= Process(target=dance,name = '2')
    #开启
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    #修改子进程名的第二种方式
    p1.name = '3'
    p2.name = '4'
    #访问name属性
    print('p1:',p1.name,'p2:',p2.name)
    #查看子进程1的进程编号
    print(p1.pid)
    print(p2.pid)
    print(os.getpid())
    print(os.getppid())
    #cmd命令提示符窗口输入tasklist可以查看电脑里面进程的命令
    #Ctrl+F查找
    #pycharm64软件进程编号就是主进程的父进程编号

# 进程间不共享全局变量
from multiprocessing import Process
import time
li = []
def wdata():
    for i in range(5):
        li.append(i)
        time.sleep(0.1)
    print(li)
def rdata():
    print(li)
#1防止别人导入文件的时候执行main里面的方法
#2防止windows系统递归创建子进程
if __name__ == '__main__':
    p1 = Process(target=wdata)
    p2 = Process(target=rdata)
    p1.start()
    p2.start()
    #p2读取是空的，进程不共享全局变量
