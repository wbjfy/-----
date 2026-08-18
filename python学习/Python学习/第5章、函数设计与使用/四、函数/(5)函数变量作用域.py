# 变量的作用域指的是变量的作用范围(标识这个变量在哪里可以使用，在哪不可以使用)
# 定义函数
num = 100
def circle_area(r):
    pi = 3.14
    area = pi * r * r
    # 局部变量num
    num = 10000
    print(num)
    return area
count = 0
# 调用函数
# print(pi)   #无法调用局部变量
c_area = circle_area(10)
print(c_area)
print(num)
# 全局变量:在函数之外定义的变量，称之为全局变量，在整个文件中(包括函数内)都可以使用(通常定义在文件的顶部)
# 局部变量:在函数内部定义的变量,称之为局部变量,只能在该函数内部使用，外部无法访问(函数执行完毕后,会自动销毁其内部局部变量)
#
#global关键字
# global关键字用于明确告诉Python解释器，在函数中要使用全局变量，使得可以在函数内部修改全局变量的值
num1 = 1
def fun1():
    num1 = 100
    print(num1)
fun1()
print(num1)

num2 = 1
def fun2():
    global num2
    num2 = 10000
    print(num2)
fun2()
print(num2)
