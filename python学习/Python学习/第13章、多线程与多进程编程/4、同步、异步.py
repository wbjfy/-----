# 同步与异步指的是提交任务的两种方式:
# 同步调用:提交完成任务后，就在原地等待，直到任务运行完毕后，拿到任务的返回值，才能继续执行下一行代码
# 异步调用:提交完任务后，不在原地等待，直接执行下一行代码
# 同步:我等你 （当你告诉（拿到任务的返回值）我已经执行完，那我再往下执行）
# 异步:只管提交任务执行  系统会通知任务是否执行完毕

#异步:不用等待当前进程执行完毕，随时根据系统调度来进行进程切换
import os
import time
from multiprocessing import Pool

def learn(n):
    print('我们在做学术交流')
    time.sleep(2)
    return  n**2

if __name__ == '__main__':
    #创建进程池，最佳进程数为3
    p = Pool(3)
    list1 = []
    for i in range(6):
        #apply_async异步
        result = p.apply_async(learn,args=(i,))  #learn函数名，i为函数learn的参数
        #把结果添加到list1泪飙里
        list1.append(result)
    #关闭进程池，关闭后p不再接收新的请求
    p.close()
    #等待p中所有子进程执行完成，必须放在close语句之后
    p.join()
    for j in list1:
        #使用get来获取apply_async的结果
        print(j.get())

# 同步:apply  同步阻塞，等待子进程执行结束后，再进行下一个进程
import os
import time
from multiprocessing import Pool
def learn(n):
    print('我们在做学术交流')
    time.sleep(2)
    return  n**2

if __name__ == '__main__':
    p = Pool(3)
    list1 = []
    for i in range(6):
        result = p.apply(learn, args=(i,))
        list1.append(result)
    print(list1)
