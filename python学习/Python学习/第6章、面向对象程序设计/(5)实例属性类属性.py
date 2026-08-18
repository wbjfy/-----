# 属性分为:
# 实例属性:实例属性属于每个具体对象的属性，每个对象都是独立的(各个对象特有的数据)
# 类属性:类属性是属于类本身的属性，所有实例共享的。(所有对象共享的数据或配置)
class Car:
    wheel = 4 # 轮胎数量
    tax_rate = 0.1 #购置税
    #这个就是类属性  调用 类型.属性名
    def __init__(self,brand,name,price):
        self.brand = brand
        self.name = name
        self.price = price
        #这里的self.属性名  就是实例属性
# 说明:通过实例查找属性时，会先查找实例属性，实例属性不存在时，再查找类属性
# 访问类属性也可以通过   类名.属性
