# 1、通过type()语句来得到数据的类型，具体语法为：type(要查看类型的数据)
print(type(100))
print(type(3.14))
print(type('hell0'))
print(type(None))
num = 5.0
print(type(num))
# 2、通过isinstance()检测数据是否属于指定的类型，返回的是一个bool值，具体语法为：isinstance(数据，类型)
num = 5.0
print(isinstance(num, int))