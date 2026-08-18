# 包:本质就是一个文件夹,该文件夹中可以包含若干python模块(.py文件),文件夹下还包含了一个__init__.py
# 作用:模块文件较多时,用来管理多个模块(包的本质也是一个模块)
# import 包名.模块名            import utils.my_fun                        包名.模块名.功能名    utils.my_fun.log_separator1()
# from 包名 import 模块名       from utils import my_fun                   模块名.功能名        my_fun. log_separator1()
# from 包名 import *           from utils import *                        模块名.功能名        my_fun.log_separator1()
# from 包名.模块名 import 功能名  from utils.my_fun import log_separator1   功能名              log_separator1()
# from 包名.模块名 import *      from utils.my_fun import *                功能名              log_separator1()
# 当在文件中新建一个名字为__init__.py的文件则这个文件夹就会变成包
# 或者直接创建软件包
# 注意:在通过'from 包名 import *' 导入全部模块的时候,需要在 __init__.py文件中添加 '__all__ = ['模块名']',控制允许导入的模块列表
# 相对路径:会在当前文件夹里找包
# 绝对路径:例如 from 第一章Python核心语法.包名 import 模块名
