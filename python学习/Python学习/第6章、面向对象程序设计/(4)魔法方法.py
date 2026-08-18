# 魔法方法是指Python中提供的以双下划线开头和结尾的特殊方法，用于定义类的特殊行为，比如:__init__。
# 魔法方法是不需要我们手动调用的，Python会在合适的时机自动调用
# __init__              初始化方法
# __del__               最后自动调用  析构函数
# __str__               字符串表示的方法
# __eq__                比较两个对象是否相等(equal)
# __lt__,__le__,__gt__,__ge__   支持比较两个对象的大小(小于(less than)，小于等于(less than or equal),大于(greater than),大于等于(greater than or equal))
# 常见的魔法方法
# 1__new__()：在内存中为对象分配空间并返回对象的引用
# 2__init__()：初始化对象或给属性赋值（构造函数）
# 3__doc__()：类的描述信息
# 4__module__()：表示当前操作对象所在模块
# 5__class__()：表示当前操作对象所在的类
# 6__str__()：对象的描述信息
# 7__del__()：删除对象（析构函数）
# 8__call__()：使一个实例对象成为一个可调用的对象
# 9__dict__()：返回对象具有的属性和方法

class Car:
    def __init__(self,brand,name,price):
        self.brand = brand
        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.brand} {self.name} {self.price}"
    def __eq__(self,other):
        return self.brand == other.brand and self.name == other.name and self.price == other.price
    def __lt__(self,other):
        return self.price < other.price
    def __del__(self):
        print('销毁')
c1 = Car('BMW','X5',500000)
print(c1)
c2 = Car('BMW','X5',500001)
print(c2)

print(c1 == c2)
print(c1 < c2)
# 更多方法看书148页！！！！！！！！！！！！