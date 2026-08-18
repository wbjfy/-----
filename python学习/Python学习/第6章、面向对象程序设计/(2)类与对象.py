# 类:描述的是一组具有相同属性(特征)和方法(功能/行为)的模板。
# 对象:对象是类的实例，是基于类创建出来的(实例对象)。
# 对象是由类创建出来的，创建对象的过程，也称为对象的实例化，一个类可以创建无数个对象
# 类的定义
# class 类名:
#     pass
# 创建对象
# 对象名 = 类名()
# 动态添加属性
# 对象名.属性名1 = 属性值1
# 对象名.属性名2 = 属性值2
# 说明:类名的命名规范，遵循大驼峰命名法，每个单词的首字母都是大写，单词之间没有分隔符，比如:UserInfo，UserAccount
class Car:
    pass
c1 = Car()
c1.brand = "BMW"
c1.name = "X5"
c1.price = 500000
print(c1.__dict__)
# 说明:__dict__是Python中用户自定义类实例的一个特殊属性，用于以字典形式存储对象的属性
#
# 推荐写法
# class 类名:
#     def __init__(self,参数列表):
#         self.属性名 = 参数值
#         self.属性名 = 参数值
# 对象名 = 类名(参数列表)
class Car:
    # def 定义在外面称之为函数，定义在类中的函数称之为方法
    def __init__(self,c_brand,c_name,c_price):
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
# __init__:初始化方法，对象创建后自动调用，主要用于设置对象的初始状态(设置对象属性)
# self:方法的第一个参数，表示当前创建的实例对象
ci = Car("BMW","X5",100000)
print(ci.__dict__)