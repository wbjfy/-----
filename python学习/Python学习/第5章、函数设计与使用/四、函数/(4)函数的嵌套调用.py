# 嵌套调用指的是在一个函数中，又调用了另一个函数
# 函数调用遵循栈结构，最后被调用的函数最先返回LIFO(Last In First Out,后进先出)
def funa():
    print('a     1')
    funb()
    print('a     2')
def funb():
    print('b     1')
    func()
    print('b     2')
def func():
    print('c     1')
funa()