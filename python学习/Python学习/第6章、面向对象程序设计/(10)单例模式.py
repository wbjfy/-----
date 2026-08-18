# __init__()和  __new__()
# __init__():初始化对象
class Test(object):
    def __init__(self):
        print('这是__init__()')
te = Test()
# 会直接调用但不是最先  第一个调用的是__new__()
# __new__():object基类提供的内置的静态方法
# 作用：1在内存中为对象分配空间  2返回对象的引用
class Test(object):
    def __init__(self):
        print('这是__init__()')
    def __new__(cls, *args, **kwargs):     #cls 代表类本身
        print('我是__new__()')
        #对父类方法进行扩展
        res = super().__new__(cls)      #方法重写，res里面保存的是实例对象的引用
        return res
#注意：重写__new__()一定要return super().__new__(cls)，否则python解释器得不到分配空间的对象引用，就不会调用__init__()
te1 = Test()
print(te1)
# 此时不再显示__init__()
# 若打印te会显示None
# 内存地址被覆盖
# 要用重写来表达
# 总结：__init__() 和 __new__()
# 1__new__()是创建对象，__init__()是初始化对象
# 2__new__()是返回对象引用，__init__()定义实例属性
# 3__new__()是类级别的方法，__init__()是实例级别的方法

# 单例模式
# 含义：一种常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在。当你希望在整个系统中，某个类只能出现一个实例时，单例模式就能派上用场
# 优点：节省内存空间    缺点：多线程访问的时候容易引发线程安全问题
# 方式
# 1通过@classmethod
# 2通过装饰器实现
# 3通过重写__new__()实现(重点)
# 4通过导入模块实现
class A(object):
    pass
a1 = A()
print(a1)
a2 = A()
print(a2)    #内存地址发生变化说明时不同的对象
#实现单例模式  对象的内存地址都是一样的，只有一个对象
# 通过重写__new__()实现单例模式
# 设计流程
# 1定义一个类属性，初始值为None，用来记录单例对象的引用
# 2重写__new__()方法
# 3进行判断，如果类属性是None，把__new__()返回的对象引用保存进去
# 4返回类属性中记录的对象
class Singleton(object):
    #记录第一个被创建的对象的引用
    obj = None     #类属性
    def __new__(cls, *args, **kwargs):
        print('这是__new__()方法')
        #判断类属性是否为空
        if cls.obj == None:
            cls.obj = super().__new__(cls)
        return cls.obj
    def __init__(self):
        print('我是__init__()')
s = Singleton()
print(s)
s2 = Singleton()
print(s2)
# 单例模式：每一次实例化所创建的对象都是同一个，内存地址都一样
# 通过导入模块实现单例模式
# 设置一个模块在另一处导入不管设置什么名字内存地址都一样
# from 模块名 import 功能名 as 起名字1
# from 模块名 import 功能名 as 起名字2
# 此时打印两个都是相同地址
# 应用场景
# 1回收站对象
# 2音乐播放器，一个音乐播放软件负责音乐播放的对象只有一个
# 3开发游戏软件      场景管理器
# 4数据库配置、数据库连接池的设计
