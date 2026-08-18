# N的阶乘
# 定义一个函数，根据传入的数字，计算该数字阶乘的结果。
# 递归调用：在函数中自己调用自己         一定要有终结点
def jc(n):
    if n == 1:
        return 1
    else:
        return n * jc(n-1)

print(jc(10))