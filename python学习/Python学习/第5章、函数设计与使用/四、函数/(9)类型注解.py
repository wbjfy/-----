# 类型注解时Python中的一种语法特性，用于明确标识变量、函数参数和返回值的数据类型，从而使代码更清晰、更安全、更易于维护
# 指定类型不能改变
a:int = 695
score:float = 98.5
hobby:str = "Python"
flag:bool = True
pic:None = None
names:list[str | int] = ["A","B","C"]  #或者 --->两个类型均可
phones:set[str] = {'1243151251235','155124523154123'}
options:dict[str,int] = {'count':0,'total':0}
goods:tuple[str,int,int] = ('手机',5999,1)
# 类型推断
# 指的是Python解释器自动推断出变量、表达式或函数返回值的数据类型的能力，而无需开发者显示声明
b = [1,2,3,4]
b.append('a')   #进行类型推断提醒类型不同但不影响运行
print(b)
# 注意:在对变量进行直接赋值，或者涉及到变量的运算、容器的推导等场景时，解释器会自动推导出变量的类型。
