# os 模块
# 作用：用于和操作系统进行交互
# 通用操作：
# 1获取平台信息
# 2对目录的操作
# 3判断操作

import os
#1 os.name   #指示正在使用的工作平台(返回操作系统类型)
print(os.name)
#对于Windows,返回nt,对于Linux,返回posix
#2 os.getenv(环境变量名称)    #读取环境变量
print(os.getenv('path'))
#3 os.path.split()   #把目录名和文件名分离，以元组的形式接收，第一个元素时目录路径，第二个元素时文件名
print(os.path.split(r'G:\学习1\1.py'))
o = os.path.split((r'G:\学习1\1.py'))
print(o[0])
#4 os.path.dirname   #显示split分割的第一个元素，即目录
print(os.path.dirname(r'G:\学习1\1.py'))
#5 os.path.basename   #显示split分割的第二个元素，即文件名
print(os.path.basename(r'G:\学习1\1.py'))
#6 os.path.exists()    #判断路径(文件或目录)是否存在，存在返回True，不存在返回None
print(os.path.exists(r'G:\学习1\1.py'))
#7 os.path.isfile()  #判断是否存在文件
print(os.path.isfile(r'G:\学习1\1.py'))
print(os.path.isfile(r'G:\学习1'))
#8 os.path.isdir()  #判断目录是否存在
print(os.path.isdir(r'G:\学习1\1.py'))
print(os.path.isdir(r'G:\学习1'))
#9 os.path.abspath()   #获取当前路径下的绝对路径
print(os.path.abspath(r'1.py'))
#10 os.path.isabs()   #判断是否时绝对路径
print(os.path.isabs(r'G:\学习1\1.py'))
