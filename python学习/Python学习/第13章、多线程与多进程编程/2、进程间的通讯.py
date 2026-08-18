# 进程间的通信
# Queue(队列)
# q.put()：放入数据
# q.get()：取出数据
# q.empty()：判断队列是否为空
# q.qsize()：返回当前队列包含的消息数量
# q.full()：判断队列是否满了
from queue import Queue
#初始化一个队列对象
q = Queue(3)   #最多可以接收三条消息，没写或者是负值就代表没有上限，直到内存的尽头
q.put('爱你到老')
q.put('你在做梦')
print(q.full())
q.put('年轻人不讲武德')
print(q.full())
print(q.qsize())
print(q.get())   #获取队列的一条消息，然后将其从队列中移除
print(q.get())
print(q.empty())
print(q.get())
print(q.empty())
print(q.qsize())

from multiprocessing import Process,Queue
import time
li = ['张三','李四','王五','赵六']
def wdata(q1):
    for i in range(5):
        print(f'{i}以及被放入')
        q1.put(i)
        time.sleep(0.1)
    print(li)
def rdata(q2):
    while True:
        #判断是否为空，队列为空就退出循环
        if q2.empty():
            break
        else:
            print(q2.get())
    print(li)
#1防止别人导入文件的时候执行main里面的方法
#2防止windows系统递归创建子进程
if __name__ == '__main__':
    #创建队列对象
    q = Queue()
    p1 = Process(target=wdata, args=(q,))
    p2 = Process(target=rdata, args=(q,))
    p1.start()
    p1.join()
    p2.start()