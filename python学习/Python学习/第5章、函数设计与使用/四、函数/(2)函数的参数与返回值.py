# 计算圆的面积
def circle_area(r):
    area = 3.14 * (r ** 2)
    return area
def circle_area2(r):
    return round(3.14 * (r ** 2),2),round(2 *3.14 * r,2)  #若有多个返回值用,隔开  round(数值,留几位小数)四舍五入
print(circle_area(5))
a,b = circle_area2(10)   #解包
print(a)
print(b)
# 计算长方形的面积
def rectangle_area(l,w):
    area = l * w
    return area
print(rectangle_area(5,3))
# 注意:函数定义时如果有多个参数，多个参数之间使用(,)分隔。
# 注意:return语句只有返回功能，而没有输出打印的功能，需要结构print()函数实现.
# 形参(形式参数):函数定义时括号里的参数，只能在函数内使用(局部变量)
# 实参(实际参数):函数在实际调用时传入的参数