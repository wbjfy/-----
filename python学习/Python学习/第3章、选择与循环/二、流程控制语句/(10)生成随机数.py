import random
a = random.randint(1, 100)
# while True:
#     b = int(input('亲输入猜测的数：'))
#     if b == a:
#         print('恭喜你')
#         break
#     elif b > a:
#         print('猜大了')
#     else:
#         print('猜小了')
b = 50
c = 0
d = 100
while True:
    c += 1
    if a == b:
        print('恭喜')
        break
    if a > b:
        b = int((b + d)/2)
        print('猜小了')
    else:
        d = b
        b = int(b/2)
        print('猜大了')
print(c)