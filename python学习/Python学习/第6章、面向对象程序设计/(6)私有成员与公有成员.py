# 如果成员名图两个下划线开头但不以两个下划线结尾，不能在类的外部不能直接访问
class A:
    def __init__(self,value1=1,value2=2):  #构造方法
        self.value1 = value1
        self.__value2 = value2  #创建私有数据成员
    def setValue(self,value1,value2):   #在成员方法中访问私有数据成员
        self.value1 = value1
        self.__value2 = value2
    def show(self):
        print(self.value1)
        print(self.__value2)
a = A()
print(a.value1)
print(a._A__value2)   #在外部访问对象的私有数据成员,不建议
a.show()

# _xxx:以单下划线开头的对象叫做保护成员，模块中这样的对象默认不能用 from module import * 导入
# __xxx__:前后个两个下划线表示系统预定义的特殊成员，不能随意定义和增加，只能修改或重新实现其功能
# __xxx:私有成员在外部可以通过 对象名._类名__xxx来访问
div, _ = divmod(2024,20)
print(div)
# 封装
# 面向对象三大特性：封装、继承、多态
# 封装：将复杂的信息、流程给包起来，内部处理，让使用者只需要通过简单的操作步骤，就能实现隐藏对象中一些不希望被外部所访问到的属性或方法
# 隐藏属性（私有权限），只允许在类的内部使用，无法通过对象访问
# 在属性名或方法名前面加上两个下划线__
# 隐藏属性实际上时将名字修改为：_类名__属性名
# 在类的内部访问也可以访问到
# 如    def introduce():
#                Person.__age = 18
#                print(f'{Person.__age}')
# 普通属性/方法，如果是类中定义的，则类可以在任意地方使用
# 单下划线开头，声明私有属性/方法，如果定义在类中，外部可以使用，子类也可以继承，但是在另一个py文件中通过from xxximport *导入的时候，也无法导入
# 一般是为了避免与python关键字冲突采用的命名方法
# 双下划线开头，隐藏属性，如果定义在类中，无法在外部直接访问，子类不会继承，要访问只能通过间接的方式，另一个py文件中通过from xxximport *导入的时候，也无法导入
# 这种命名一般是python中的魔术方法或属性，都是有特殊含义或功能的，自己不要轻易定义
class Person:
    name = 'bingbing'
    __age = 18               #隐藏属性
    _sex = '女'                #私有属性
pe = Person()
print(pe._sex)
print(pe._Person__age)

class Man:
    def __play(self):               #隐藏方法
        print('玩手机')
    def funa(self):                   #平平无奇的实例方法
        print('平平无奇')

    def funa1(self):
        print('平平无奇')
        Man.__play(self)
        self.__play()
ma = Man()
ma.funa()
ma.funa1()
# 若在实例方法中调用隐藏方法则可以调用出来
# 私有方法
class Girl:
    def _buy(self):       #私有方法
        print('123')
gi = Girl()
gi._buy()
