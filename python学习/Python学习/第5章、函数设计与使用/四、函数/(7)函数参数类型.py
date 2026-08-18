# 普通参数:数字、布尔、字符串、列表、元组、集合、字典等。
# 特殊参数:函数
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def calc(x,y,oper):
    return oper(x,y)
result = calc(2,3,add)
print(result)