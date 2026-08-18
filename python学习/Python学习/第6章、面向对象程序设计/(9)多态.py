# 多态：同一种行为具有不同的表现形式
# 前提：1继承  2重写
# 特点：
# 1不关注对象的类型，关注对象具有的行为，也就是对象的实例方法是否同名
# 2多态的好处可以增加代码的外部调用灵活度，让代码更加通用，兼容性比较强
# 3不同的子类对象，调用相同的父类方法，会产生不同的执行结果
class Animal(object):
    """父类；动物类"""
    def shout(self):
        print('动物会叫')
class Dog(Animal):
    """子类一；狗类"""
    def shout(self):
        print('我是小狗')
class Cat(Animal):
    """子类二；狗类"""
    def shout(self):
        print('小狗')
cat = Cat()
cat.shout()
dog = Dog()
dog.shout()
# 多态性：一种调用的方式，不同的执行结果
class Animal(object):
    def eat(self):
        print('吃饭')
class Pig(Animal):
    def eat(self):
        print('吃饭1')
class Dog(Animal):
    def eat(self):
        print('吃饭2')
#多态性：定义一个统一的接口，一个接口多种实现
def test(abc):     #括号里都行
    abc.eat()
animal = Animal()
pig = Pig()
dog=Dog()
test(pig)
test(dog)
test(animal)
#test函数传入不同的对象，执行不同对象的eat方法
