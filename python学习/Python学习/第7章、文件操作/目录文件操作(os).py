# 具体看书166页
# 目录常用操作
# 导入模块
# import os
# 1文件重命名：os.rename(旧名字,新名字)
# 2文件删除：os.remove(目标文件名)
# 3创建文件夹：os.mkdir(文件夹名)
# 4获取当前目录：os.getcwd()
# 5获取目录列表：os.listdir(目录)
# 6删除文件夹：os.rmdir(文件夹名)

import os
# 1  os.rename()
os.rename('test.py','text.py')
# 2  os.remove()
os.remove('test.py')
# 3  os.mkdir()
os.mkdir('text.py')
# 4  os.rmdir()
os.rmdir('text.py')
# 5  os.getcwd
print(os.getcwd())
# 6  os.listdir()
print(os.listdir())      #默认获取当前目录列表
print(os.listdir('../'))   #获取上一级目录列表
