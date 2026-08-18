# 文件读写
# 文件就是存储在某种长期储存设备上的一段数据
# 基础操作
# 1打开文件
# 2读、写文件
# 3关闭文件
# 注意：可以只打开和关闭文件，不进行任何读写操作
# 文件对象的方法
# 1open()：创建一个file对象，默认是以只读模式打开
# 2read(n)：表示从文件中读取的数据的长度，没有传n值就默认一次性读取文件的所有内容
# 3write()：将指定内容写入文件
# 4close()：关闭文件
# 属性
# 文件名.name：返回要打开的文件的文件名，可以包含文件的具体路径
# 文件名.mode：返回文件的访问模式
# 文件名.closed：检查文件是否关闭，关闭返回True
# #打开文件
f = open('test.py')
print(f.name)    #文件名
print(f.mode)    #文件访问模式
#关闭文件
f.close()
print(f.closed)

# 读写操作
# 1read(n)：读取文件
# 2readline()：一次读取一行内容
# 3readlines()：按照行的方式一次性读取全部内容
# 4write()：写入内容
#
# 1read(n)：n表示从文件中读取的数据长度，没有传n值或传的是负数就默认一次性读取文件的所有内容
f = open('test.py')
# print(f.read())
print(f.read(6))
f.close()
# 2readline()：一次读取一行内容，方法执行完，会把文件指针移到下一行，准备再次读取
f = open('test.py')
# print(f.readline())
# print(f.readline())
# print(f.readline())
while True:
    text = f.readline()#读取
    #读取不到内容退出循环
    if not text:
        break
    print(text)
f.close()
# 3readlines()：按照行的方式把文件内容一次性读取，返回的是一个列表，每一行的数据就是列表中的元素
f = open('test.py')
text = f.readlines()
# print(text)
# print(type(text))
for i in text:
    print(i)
f.close()

# 访问模式            可操作             若文件不存在                是否覆盖
# r                  只能读               报错                       -
# r+                 可读可写             报错                       是
# w                   只能写              创建                       是
# w+                  可读可写            创建                        是
# a                   只能写              创建                      否，追加写
# a+                  可读可写            创建                      否，追加写
# +：表示可以同时读写某个文件使用时会影响文件的读写效率，开发过程中更多时候会以只读、只写的方式来操作文件
#
# r：只读模式（默认），文件必须存在，不存在就会报错
# w：只写模式，文件存在就会先清空文件内容，再写入添加内容，不存在就创建新文件
# a：追加模式，不存在就创建新文件写入，存在则在原有内容基础上追加新内容
f = open('test','r+')
f.write('...')
print(f.read())
f.close()
# 文件指针：标记从哪个位置开始读取数据
# 文件定位操作  tell()和seek()
# tell()：显示文件当前位置，即文件指针当前位置
# seek(offsrt,whence)：移动文件读取指针到指定位置
# offset：偏移量，表示要移动的字节数
# whence：起始位置，表示移动字节的参考位置，默认时0，0代表文件开头作为参考位置，1代表当前位置作为参考位置，2代表将文件结尾作为参考位置
# seek(0,0)就会把文件指针移动到文件开头
f = open('test','w+')
f.write('...,,,')
a = f.tell()
print(a)
f.seek(0,0)
b = f.tell()
print(b)
print(f.read())
f.close()

# with open
# 作用：代码执行完，系统会自动调用f.close()，可以省略文件关闭步骤
with open('test','w+') as f:
    f.write('123124')

# 编码格式
# 注意：file对象的encoding参数的默认值与平台有关，比如Windows上默认字符编码为GBK
# encoding表示编码集，根据文件的实际保存编码进行获取数据，对于我们而言，使用更多的时utf-8
with open('test','w+',encoding='utf8') as f:
    f.write('你好')
    f.seek(0)
    print(f.read())
# 案例：图片复制‘rb’
# 1读取图片
# 图片是一个二进制文件，想要写入必须先拿到
# 2写入图片
#读取文件
with open(r'D:\25人工智能\名字','rb') as f:
    a = f.read()
    print(a)
#将读取到的内容写入到文件中
with open(r'G:\学习1\venv\名字','wb') as f:
    f.write(a)
