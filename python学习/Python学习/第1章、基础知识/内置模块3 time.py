# time模块
import time
#三种时间表示
#1 时间戳(timestamp)
#2 格式化的时间字符串(format time)
#3 时间元组(strut_time)

#1 time.sleep()  #延时操作，以秒为单位
print(12)
time.sleep(2)
print(13)
#2 time.time()  #获取到当前的时间戳:以秒计算，从1970年1月1日00:00:00开始到现在的时间差
print(type(time.time()))    #返回的是浮点型
#3 time.localtime()  #将一个时间戳转换为当前时区的struct_time
print(time.localtime())
#4 time.asctime()    #获取系统当前时间,把struct_time换成固定的字符串表达式
print(time.asctime())
#5 time.ctime()   #获取系统当前时间，把时间戳转换成固定的字符串表达式
t = time.time()
print(time.ctime(t))
#6 time.strftime(格式化字符串,struct_time)    #将struct_time转换成时间字符串
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
#7 time.strptime(时间字符串,格式化字符串)     #将时间字符串转换成struct_time
print(time.strptime("2025-11-02",'%Y-%m-%d'))
