# 函数的说明文档(Docstring)是写在函数开头，用三个引号包裹的字符串，用于解释函数的功能、参数、返回值等信息，方便调用者清楚函数的具体作用及细节
def circle_area_len(r):
    """
    该函数用于根据圆的半径，计算圆的面积和圆的周长
    :param r: 圆的半径
    :return: 圆的面积,圆的周长
    """
    return 3.14 * r * r,2 * 3.14 * r
al = circle_area_len(10)
print(al)
help(circle_area_len)   #将函数说明文档调用出来
