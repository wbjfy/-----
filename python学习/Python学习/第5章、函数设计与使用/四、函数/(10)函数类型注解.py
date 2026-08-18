# 为函数添加类型注解，其实主要就是为函数的参数和返回值添加类型注解，具体语法如下
def calc(scores : list[int]) -> float:
    #              参数类型        返回值类型
    return sum(scores) / len(scores)