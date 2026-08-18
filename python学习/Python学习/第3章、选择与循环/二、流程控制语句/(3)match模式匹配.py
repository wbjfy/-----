# 结构模式匹配就是用一个清晰的模板取精准的匹配数据的结构和内容，匹配成功则执行响应操作
day = input('请输入星期几(1-7)')
if day == '1':
    print(1)
elif day == '2':
    print(2)
elif day == '3':
    print(3)
elif day == '4':
    print(4)
elif day == '5':
    print(5)
elif day == '6':
    print(6)
elif day == '7':
    print(7)
else:
    print("输入错误")

day1 = input('请输入星期几(1-7)')
match day1:
    case '1':
        print(1)
    case '2':
        print(2)
    case '3':
        print(3)
    case '4':
        print(4)
    case '5' if day == '5':   #可以加上if判断
        print(5)
    case '6' | '7':        #表示或的关系
        print(67)
    case _:                #匹配其他所有情况
        print('输入错误')