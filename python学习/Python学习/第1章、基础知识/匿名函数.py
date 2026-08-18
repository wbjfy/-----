# 匿名函数指的是没有名称的函数，需要通过lambda表达式来声明函数，可以简化简单函数的编写(单行表达式)
# 定义匿名函数
# lambda 参数列表 : 函数体
out_line = lambda : print("Hello World")
add = lambda x,y : x + y
out_line()
print(add(1,2))
# 注意:函数逻辑比较简单(单行表达式)且只在一个地方使用时，可以考虑使用匿名函数,简化书写(通常作为高阶函数的参数使用)
# 注意:匿名函数中可以返回结果，也可以不返回结果。返回结果时，不需要写return，表达式的运行结果就是要返回的结果
list1 = ['C','B2','A1','ASD3','gad14','s321']
list1.sort()
print(list1)
list1.sort(key = lambda item : len(item))
print(list1)
list1.sort(key = lambda item : len(item),reverse = True)
print(list1)