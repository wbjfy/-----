# greenlet
# 为了更好的使用协程来完成多任务，python中的greenlet模块对其封装，从而使得切换任务变得更加简单
# 安装命令：pip install greenlet
# 安装:pip install 模块名
# 卸载:pip uninstall 模块名
# 查看已安装的模块:pip list
# 注意:greenlet属于手动切换，当遇到IO操作，程序会阻塞，而不能进行自动切换
# 通过greenlet实现任务的切换
# 导入greenlet模块
from greenlet import greenlet
def sing():
    print('在唱歌')
    g2.switch()
    print('唱完歌了')
def dance():
    print('在跳舞')
    print('跳完了')
    g1.switch()
if __name__ == '__main__':
    #创建协程对象 greenlet(任务名)
    g1 = greenlet(sing)
    g2 = greenlet(dance)
    g1.switch()   #切换到给g1中去运行
    g2.switch()

# gevent：遇到IO操作时，会进行自动切换，属于主动切换
# 注意：文件命名不要和第三方模块或内置模块重名
# 使用
# gevent.spawn(函数名)：创建协程对象
# gevent.sleep()：耗时操作
# gevent.join()：阻塞，等待某个协程执行结束
# gevent.joinall()：等待所有协程对象都执行结束再退出，参数是一个协程对象列表

# sleep
import gevent
from greenlet import greenlet
import time

def sing():
    print('唱歌')
    gevent.sleep(2)
    print('完毕')
def dance():
    print('跳舞')
    gevent.sleep(3)
    print('ok')
if __name__ == '__main__':
    #1创建协程对象
    g1 = gevent.spawn(sing)
    g2 = gevent.spawn(dance)
    #2阻塞，等待协程执行结束
    g1.join()   #等待g1对象执行结束
    g2.join()

# joinall()：等待所有协程都执行结束再退出
import gevent
from greenlet import greenlet

def sing(name):
    for i in range(1,4):
        gevent.sleep(1)
        print(f'{name}在唱歌，被送走{i}次')
if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(sing,'bingbing'),
        gevent.spawn(sing,'冰冰'),
    ])

# monket补丁：拥有在模块运行时替换的功能
import gevent
from greenlet import greenlet
import time
from gevent import monkey

monkey.patch_all()    #将用到的time.sleep()代码替换成gevent里面自己实现耗时操作的gevent.sleep()代码
#注意：monkey.patch_all() 必须放在被打补丁的前面

def sing(name):
    for i in range(1,4):
        time.sleep(1)
        print(f'{name}在唱歌，被送走{i}次')
if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(sing,'bingbing'),
        gevent.spawn(sing,'冰冰'),
    ])

# 总结
# 1线程时CPU调度的基本单位，进程时资源分配的基本单位
#  2进程、线程和协程对比
#     进程：切换需要的资源最大，效率最低
#     线程：切换需要的资源一般，效率一般
#     协程：切换需要的资源最小，效率最高
# 3多线程适合IO密集型操作（文件操作、爬虫），多进程是个CPU密集型操作（科学及计算、对视频进行高清解码、计算圆周率等）
# 4 进程、线程、协程都是可以完成多任务的，可以根据自己实际开发的需要选择使用
