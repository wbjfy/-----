# 静态方法
# 使用@staticmethod来进行修饰，镜头方法没有self，cls参数的限制
# 静态方法与类无关，可以被转换成函数使用
class Person:
    @staticmethod    #静态方法
    def study():
        print('学习')
Person.study()
pe = Person()
pe.study()
# 若添加参数不必再打出Person.name
class Person:
    @staticmethod    #静态方法
    def study(name):
        print(f'{name}学习')
Person.study(1)
pe = Person()
pe.study(1)
# 取消不必要的参数传递，有利于减少不必要的内存占用和性能消耗

# 类方法
# 使用装饰器@classmethod来标识为类方法，对于类方法，第一个参数必须是类对象，一般是以cls作为第一个参数
class Person:
    @classmethod
    def sleep(cls):
        print(cls)     #cls代表类对象本身，类本质上就是一个对象
        print('睡觉')
Person.sleep()
# 当方法中需要使用到类对象（如访问私有类属性等），定义类方法。类方法一般是配合类属性使用
# 总结：
# 1实例方法：方法内部访问实例属性，方法内部可以通过类名.类属性名来访问类属性
# 2静态方法@staticmethod：方法内部，不需要访问实例属性和类属性，如果要访问类属性，通过类名.类属性访问，不能访问实例属性
# 3类方法@classmethod：方法内部只需要访问类属性，可以通过cls
# 1. 实例方法 (Instance Method)
# 特点：
# · 第一个参数必须是 self，指向实例本身
# · 可以访问和修改实例属性
# · 可以访问类属性
# · 通过实例调用
# 2. 类方法 (Class Method)
# 特点：
# · 使用 @classmethod 装饰器
# · 第一个参数必须是 cls，指向类本身
# · 可以访问和修改类属性
# · 不能访问实例属性
# · 可以通过类或实例调用
# 3. 静态方法 (Static Method)
# 特点：
# · 使用 @staticmethod 装饰器
# · 不需要特定的第一个参数（没有 self 或 cls）
# · 不能访问实例属性或类属性
# · 类似于普通函数，但属于类的命名空间
# · 可以通过类或实例调用
#
#
# 特性             实例方法                类方法                     静态方法
# 装饰器            无                     @classmethod            @staticmethod
# 第一个参数      self (实例)              cls (类)                 无特殊参数
# 访问实例属性       ✅                       ❌                     ❌
# 访问类属性         ✅                       ✅                     ❌
# 修改类状态         ✅                       ✅                     ❌
# 调用方式         通过实例                 通过类或实例             通过类或实例
class Person:
    name = '小明'        #类属性：类所拥有的类属性
    def __init__(self):
        self.age = 18        #实例属性：对象私有的
    def play(self):    #实例方法
        print(f'{Person.name}在玩游戏')
    @staticmethod    #静态方法：类中的函数，形参没有限制
    def introduce():
        print(f'{Person.name}')        #静态方法能够访问到类属性但无意义
        #print(slef.name)            #会报错
        pass
    @classmethod         #类方法：针对类存在的方法
    def introduce1(cls):      #cls代表类对象本身
        print(f'{Person.name}')
        print(f'{cls.name}')
        #print(slef.name)            #会报错
pe = Person()
pe.play()
pe.introduce()
pe.introduce1()
