# 继承：让类和类之间转变为父子关系，子类默认继承父类的属性和方法
# 语法
# class 类名（父类）:
#     代码块
# 注意：继承分为单继承和多继承
# 单继承
class Person:            #父类
    def eat(self):
        print('吃饭')
    def sing(self):
        print('唱歌')
class Girl(Person):     #Person类的子类
    pass      #占位符，代码里面类下面不会写任何东西，会自动跳过，不会报错
girl = Girl()
girl.eat()
girl.sing()
# 总结:子类可以继承父类的属性和方法，就算子类没有，也可以使用父类的
# 继承的传递（多重继承）
class Father:
    def eat(self):
        print('吃饭')
    def sleep(self):
        print('睡觉')
class Son(Father):
    pass
class Grandson(Son):
    pass
grandson = Grandson()
grandson.eat()
# 继承的传递性就是子类拥有父类以及父类的父类中的属性和方法
# 方法的重写：在子类中定义与父类相同名称的方法
# 覆盖父类的方法
class Person:
    def money(self):
        print('一百万需要继承')
class Man(Person):
    def money(self):
        print('自己赚1000w')
man = Man()
man.money()
# 会优先显示自己有的
# 对父类方法进行扩展：继承父类的方法，子类也可以增加自己的功能
# 1父类名.方法名(self)
class Person:
    def money(self):
        print('一百万需要继承')
class Man(Person):
    def money(self):
        Person.money(self)
        super().money()
        print('自己赚1000w')
man = Man()
man.money()
# 2 super().方法名()             推荐使用
# super在python里面是一个特殊的类，super()是使用super类创建
# 3 super(子类名,self).方法名()
# 新式类写法
# 1 经典类:不由任意内置类型派生出的类
# 派生类:不同于父类的属性或东西
# class A:
# 新式类：继承了object类或者该类的子类都是新式类
# class A(object)
# object --对象，python为所有对象提供的基类(顶级父类)，提供了一些内置的属性和方法，可以使用dir()查看     查看方法与type一样
# 多继承：子类可以拥有多个父类，并且具有所有父类的属性和方法
class Father(object):    #父类一
    def money(self):
        print('拥有一百万')
class Mother(object):    #父类二
    def appearance(self):
        print('绝世容颜需要被继承')
class Son(Father, Mother):    #子类
    pass
son =  Son()
son.appearance()
son.money()
# 不同父类具有同名方法时
class Father(object):    #父类一
    def money(self):
        print('拥有一百万')
class Mother(object):    #父类二
    def money(self):
        print('一百二十万需要被继承')
    def appearance(self):
        print('绝世容颜需要被继承')
class Son(Father, Mother):    #子类
    pass
son =  Son()
son.appearance()
son.money()
# 此时谁在Son()里面靠前就继承谁
# 方法的搜索顺序（了解）
# python中内置属性__mro__可以查看搜索顺序
print(Son.__mro__)
# 搜索方法时，先按照__mro__的输出结果，从左往右的顺序查找
# 如果在子类中找到方法会直接执行不会再继承父类       用查找方法看顺序若左边的有了则不会去右边的继承或搜索
# 如果找到最后一个类，还没有找到方法则会报错
# 多继承弊端
# 容易引发冲突、会导致代码设计的复杂度增加