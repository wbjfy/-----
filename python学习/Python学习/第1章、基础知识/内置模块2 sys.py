import sys

# sys模块
# 作用：负责程序跟python解释器交互
# 1sys.getdefaultencoding()：获取系统默认编码格式
print(sys.getdefaultencoding())

# 2sys.path：获取环境变量的路径，跟解释器相关
print(sys.path)   #以列表的形式返回，第一项为当前所在的工作目录

# 3sys.platform：获取操作系统平台名称
print(sys.platform)

# 4sys.version：获取python解释器的版本信息
print(sys.version)
