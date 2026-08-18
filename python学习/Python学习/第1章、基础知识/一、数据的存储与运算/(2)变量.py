# 变量：程序中用来存储单个数据的容器，通常会把经常发生变化的数据存储在变量中
#定义格式：变量名 = 变量的值   num = 1114.1
#Python是动态类型语言，一个变量是可以存储不同类型的数据的(但是项目开发中，推荐变量只存储一种类型的数据)
num = 1114.1
print(num)
num = num + 1
print(num)
num = 'OK'
print(num)
num = True
print(num)
a = True
print(a)

#案例
base = 20.7 #基础播放量
incr = 50 # 每一个月的新增播放量
print('未来第一个月的播放总量：',base + incr)
print('未来第二个月的播放总量：',base + incr*2)

#一次性可以定义多个变量
base,incr = 20.7,50
print('未来第一个月的播放总量：',base + incr)
print('未来第二个月的播放总量：',base + incr*2)