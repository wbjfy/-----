# 迭代器、生成器
# 迭代器
# 可迭代对象Iterable：可以通过for i in 这类语句历遍读取数据的对象称之为可迭代对象
# 数据类型：str、list、tuple、dict、set
# 可迭代对象的条件
# 1对象实现了__iter__()方法
# 2__iter__()方法返回了迭代器对象
# for循环工作原理
# 1先通过__iter__()获取可迭代对象的迭代器
# 2对获取到的迭代器不断调用__next__()方法来获取下一个值并将其赋值给临时变量i
# isinstance()：判断一个对象是否是可迭代对象或是一个已知的数据类型
# 导入模块
from collections.abc import Iterable
#isinstance(o,t)    o：对象，t：类型，可以直接或者间接类名、基本类型或元组
st = '123412'
print(isinstance(st,Iterable))
# 迭代器Iterator
# 是一个可以记住遍历位置的对象；在上次停留的位置继续去做一些事情
# iter(),next()
# iter()：获取可迭代对象的迭代器
# next()：一个个去取元素，取完元素后会引发一个异常
# from collections.abc import Iterable
li = [1,2,3,4,5]
#创建迭代器对象
#方法一
li2 = iter(li)
#方法二
# li2 = li.__iter__()
print(li2)
#获取下一条数据
print(next(li2))
print(next(li2))
print(next(li2))
print(next(li2))
print(li2.__next__())
#取完元素后再使用next()会引发异常
# print(next(li2))

# 可迭代对象Iterable和迭代器Iterator
# 凡是可以作用有for循环的都属于可迭代对象
# 凡是可以作用于next()都是迭代器
from collections.abc import Iterator,Iterable
name = 'bingbing'
print(isinstance(name,Iterable))
print(isinstance(name,Iterator))
#可迭代对象并不一定是迭代对象
name2 = iter(name)  #将neme转换成迭代器对象
print(isinstance(name2,Iterable))
print(isinstance(name2,Iterator))
#迭代器对象一定是可迭代
# 总结：
# 可迭代对象可以通过iter()转换成迭代器对象
# 如果一个对象拥有__iter__()，是可迭代对象，如果一个对象拥有__next__()和__iter__()方法，是迭代器对象
# dir()：查看对象中的属性和方法
print(dir(name))

# 迭代器协议
# 对象必须提供一个next方法，执行该方法要么就返回迭代中的下一项，要么就引发StopIeration异常，来终止迭代
#
# 自定义迭代器类
# 两个特性：__next__()和__iter__()
class Test(object):
    #初始值是1，逐步递增1
    def __init__(self):
        self.num = 1
    def func(self):
        print(self.num)
        self.num += 1
te = Test()
print(te)
te.func()
for i in range(5):
    te.func()

class MyIterator(object):
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self   #返回的是当前迭代器类对象
    def __next__(self):
        if self.num == 10:
            raise StopIteration('终止迭代')
        self.num += 1
        return self.num
mi = MyIterator()
print(mi)
print(next(mi))
for i in mi:
    print(i)

# 生成器 Generator
# python中一边循环一边计算的机制，叫生成器
# 生成器表达式
for i in range(5):
    print(i*5)
# 列表推导式
li = [i* 5 for i in range(5)]
gen = (i*5 for i in range(5))    #列表推导式的[]改成()就成了生成器表达式
print(li)
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# 生成器函数
# python中，使用了yield关键字的函数就称之为生成器函数
# 1类似return，将指定值或者多个值返回给调用者
# 2yield语句一次返回一个结果，在每个结果中间，挂起函数，执行next()，再重新从挂起点继续往下执行，是函数的中断，并保存中断的状态
li = []
def test():
    li.append('a')
    li.append('b')
    print(li)
test()
test()
# 生成器函数
def gen():
    print('开始了')
    yield 'a'   #返回了一个‘a’，并暂停函数，在此处挂起，下一次再从此处恢复运行
    yield 'b'
    yield 'c'
gen_01 = gen()
print(gen_01)
print(next(gen_01))
print(next(gen_01))

def gen2(n):
    a = 0
    while a < n:
        yield a
        a += 1
for i in gen2(5):
    print(i)
# 使用了yield关键字就是生成器函数
def test():
    yield 1
    yield 2
    yield 3
print(test())
ta = test()
print(next(test()))    #加括号是调用函数
print(next(test()))
print(next(test()))
print(next(ta))      #从对象中取值
print(next(ta))
print(next(ta))

# 三者关系
# 可迭代对象：指实现了python迭代协议，可通过for 。。 in 。。循环遍历的对象，比如list，dict，str。。。、迭代器、生成器
# 迭代器：可以记住自己遍历位置的对象，只管体现就是可以使用next()函数返回值，迭代器只能往前，不能往后，当遍历完毕后，next()会抛出异常
# 生成器：是特殊的迭代器，需要注意迭代器不一定是生成器，他是python中提供的通过简便的方法写出迭代器的一种手段
# 包含关系：可迭代对象>迭代器>生成器
