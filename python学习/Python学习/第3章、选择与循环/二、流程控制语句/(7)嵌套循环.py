# for 元素 in 待处理数据集1:
#     循环体代码1
#     循环体代码2
#     ......
#     for 元素 in 待处理数据集2:
#         循环体代码1
#         循环体代码2
#         ......
m = int(input('请输入列数:'))
n = int(input('请输入行数:'))
for i in range(n):
    for j in range(m):
        print('* ', end='')
    print()