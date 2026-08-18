a = 0
for i in range(10):
    for j in range(10):
        a += 1
        if a == 5:
            continue
        print(a,end = ' ')
a = 0
print()
for i in range(10):
    for j in range(10):
        a += 1
        if a == 5:
            break
        print(a,end = ' ')
#break这个代码少了五次循环
# break:只能够出现在循环中，表示结束、跳出循环的含义(break跳出循环时，while后面的else中的代码将不hi执行)
# continue:只能够出现在循环中，表示中断本次循环，直接进入下一次循环