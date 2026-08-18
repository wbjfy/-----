import random

# random模块
# 作用：用于实现各种分布的伪随机数生成器，可以根据不同的实数分布来随机生成值
# 1 random.random()：产生大于0且小于1之间的小数
print(random.random())

# 2 random.uniform(a,b)：产生指定范围的随机小数
print(random.uniform(1,2))

# 3 random.randint(a,b):：产生a,b范围内的随机整数，包含开头和结尾
print(random.randint(1,6))

# 4 random.randrange(start,stop,[step])：产生start,stop范围内的整数，包含开头不包含结尾
# step：指定产生随机的步长，随机选择一个数据
print(random.randrange(2,7,2))