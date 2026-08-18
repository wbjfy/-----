# logging模块
# logging中的等级:
# LEVEL                     value                                                                    describe
# NOTEST                    0                                  不设置级别，按照父logger的级别显示日志，如果是root logger，那么就会显示所有的日志
# DEBUG                     10                                              程序的详细调试信息，调试代码会用到
# INFO                         20                                             普通信息，确定程序是否按照正常的运行
# WARNING                30                                 程序发出警告，表示发生意外想不到的事情或者指示接下来可能会出现一些问题，但是还能正常运行
# ERROR                      40                                             程序发生错误，某些功能无法运行
# CRITICAL(FATAL)       50                                             程序出现致命错误，无法运行
#
# 格式                                                                                       描述
# %(leveino)s                                                                  打印日志级别的数值
# %(leveiname)s                                                             打印日志级别名称
# %(pathname)s                                                             打印当前执行程序的路径
# %(filename)s                                                                打印当前执行程序名称
# %(funcName)s                                                             打印日志的当前函数
# %(lineno)d                                                                   打印日志的当前行号
# %(asctime)s                                                                 打印日志的时间
# %(threadName)s                                                          打印线程ld
# %(process)d                                                                 打印选程ID
# %(message)s                                                                打印日志信息
# %(name)s                                                                    打印logger的名字
# %(module)s                                                                 调用日志输出函数的模块名
# %(created)f                                                                 LogRecord的创建时间，也就是当前时间time time()
# %(msecs)d                                                                  LogRecord的创建时间的毫秒部分
# %(relativeCreated)d                                                    输出日志信息的，自logger创建以来的毫秒数

#logging模块
#1 作用:用于记录日志信息
#2 日志作用
#  (1)程序调试
#  (2)了解软件程序运行情况是否正常
#  (3)软件程序运行故障分析与问题定位
import logging


#logging默认的level就warning，也就是说logging只会显示级别大于等于warning的日志信息

#3 logging.basicConfig()    #配置root logger的参数
#   (1)  filename:指定日志文件的文件名，所有会显示的日志都会存放到这个文件中去
logging.basicConfig(filename='123.py')
#   (2)  filemode:文件的打开方式，默认是a，追加模式
logging.basicConfig(filename='123.py',filemode='w')

#   (3)  level:指定日志显示级别，默认是警告信息warning
logging.basicConfig(filename='123.py',filemode='w',level=logging.DEBUG)
#   (4)  format:指定日志信息的输出格式
logging.basicConfig(filename='123.py',filemode='w',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')
logging.debug('我是debug')
logging.info('我是info')
logging.warning('我是warning')
logging.error('我是error')
logging.critical('我是critical')
