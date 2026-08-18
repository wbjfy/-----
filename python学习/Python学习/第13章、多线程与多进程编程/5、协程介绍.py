# 协程介绍
# 协程，又称微线程，纤程。英文名Coroutine
# 协程是python中另外一种实现多任务的方式，只不过比线程更小、占用更小的执行单元（理解为需要的资源）。它自带CPU上下文。这样只要在合适的时机，我们可以把一个协程切换到另一个协程。只要这个过程中保存或恢复CPU上下文那么程序还是可以运行的
# 注意：线程和进程的操作是由程序触发系统接口，最后执行者是系统，协程的操作则是程序员
# 简单实现协程
import time
def task1():
    while True:
        yield 'a'
        yield '123'
        time.sleep(1)
def task2():
    while True:
        yield 'b'
        yield '456'
        time.sleep(1)
if __name__ == '__main__':
    t1 = task1()
    t2 = task2()
    print(next(t1))
    print(next(t2))
    print(next(t1))
    print(next(t2))
    while True:
        print(next(t1))
        print(next(t2))
# 应用场景
# 1如果一个线程里面有IO操作比较多的时候，可以用协程
#   Input/Output
# 常见IO操作：文件操作、网络请求
# 2适合高并发处理
