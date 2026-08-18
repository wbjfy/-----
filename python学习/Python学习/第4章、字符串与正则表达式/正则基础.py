# 正则基础
#
# 正则表达式
# 字符串处理工具
# 含义：记录文本规则的代码
# 注意：需要导入re模块
# 特点：
# 语法比较复杂，可读性较差
# 通用性很强，适用于多种编程语言
# 步骤
# 1导入re模块
# 2使用match方法进行匹配操作
# re.match()能匹配出以xxx开头的字符串
# 如果起始位置没有匹配成功，返回None
# 3如果上一步数据匹配成功，使用group()提取数据
# re.match(pattern, string)
#pattern 匹配的正则表达式
#string 要匹配的字符串
import re

res = re.match('冰','冰冰永远18')
print(res)
print(res.group())
#注意:match是从开始位置匹配，匹配不到就没有，且匹配的是表达式整体。

# 匹配单个字符
# .         匹配任意一个字符(除了\n)
# []        匹配[]中列举的字符
# [^]	    求反，匹配不在字符列表中的任何单个字符
# \d        匹配数字，即0~9
# \D        匹配非数字，即不是数字
# \s        匹配空白，即'空格'，tab键
# \S        匹配非空白
# \w        匹配单词字符，即a-z，A-Z，0-9
# \W        匹配非单词字符
# *	        出现任意次（0 次或无数次）
# +	        至少出现 1 次（1 次或无数次）
# ?	        至多出现一次（0 次或 1 次）
# {m}	    出现 m 次
# {m,}	    至少出现 m 次
# {m,n}	    出现 m 到 n 次
# |	        或的意思，匹配左右任意一个表达式
# ()	    分组，将括号里的多个字符视为一个单元
# ^	        匹配字符串开头
# $	        匹配字符串结尾
#
# []匹配[]中列举的字符          --常用
import re

res = re.match('[he]','hello')
print(res.group())

res = re.match('[1234]','423')
print(res.group())

#匹配0-9的第一种方法
# res = re.match('[0123456789]','423')
#匹配0-9的第二种方法
res = re.match('[0-9]','23634')
print(res.group())

#匹配0-9
res = re.match('\\d','2456')     #注意转义要么加r要么双斜杠\
print(res.group())
#匹配非数字
res = re.match('\\D','s24r')     #只要不是数字都能匹配
print(res.group())
#匹配空白，即空格tab建
res = re.match('\\s',' s24r')     #\\s\\s == 一个tab
print(res.group())
#匹配非空白
res = re.match('\\S','s24r')
print(res.group())
#匹配单词字符   a-z,A-Z,0-9,汉字
res = re.match('\\w','我24r')
print(res.group())
#匹配非单词字符
res = re.match('\\W','。我24r')
print(res.group())

# 匹配多个字符
# *：匹配前一个字符出现0次或者无限次，即可有可无
res = re.match('\\d*','2456')     #注意转义要么加r要么双斜杠\
print(res.group())

# +：匹配前一个字符出现一次或无限次，即至少一次
res = re.match('\\d+','1地主家的傻儿子')
print(res.group())

# ？：匹配前一个字符出现1次或0次，即要么有1次，要么没有
res = re.match('\\d?','12hello')
print(res.group())

# {m}：匹配前一个字符出现m次
res = re.match('\\w{3}','python')
print(res.group())

# {m,n}：匹配前一个字符出现从m到n次
# 注意：必须符合m<n的条件
res = re.match('\\w{1,4}','python')
print(res.group())

# 匹配开头和结尾
# ^：匹配字符串开头    表示对什么东西取反
res = re.match('^py','python')
print(res.group())
# 注意:在[]中表示不匹配
res = re.match('[^py]','1python')    #[^py]表示匹配了除了p、y之外的字符
print(res.group())

# $：匹配字符串结尾
res = re.match('.*g$','bingbing')
print(res.group())

# 匹配分组
# |：匹配左右任意一个表达式
res = re.match('abc|def','def')
print(res.group())

res = re.match('\\s|\\d','1234')
print(res.group())

# (ab)：将括号中字符作为一个分组
res = re.match('\\w*@(qq|163|126).com','123@qq.com')
print(res.group())

# \num：引用分组num匹配到的字符串
res = re.match('<(\\w*)><(\\w*)>\\w*</\\2></\\1>','<html><body>login</body></html>')
print(res.group())
# 注意：从外到内排序，编号从1开始

# (?p<name>)：分组起别名
# (?p=name)：引用别名为name分组匹配到的字符串
res = re.match('<(?P<L1>\\w*)><(?P<L2>\\w*)>\\w*</(?P=L2)></(?P=L1)>','<html><body>login</body></html>')
print(res.group())

#匹配网址   前缀一般是www,后缀:.com、.cn、.grg
li = ['www.baidu.com','www.python.org','http.jd.cn','www.py.en','www.abc.cn']
# res = re.match('www.\\w*.(com|cn|org)','www.baidu.com')
# print(res.group())
for i in li:
    res = re.match('www.\\w*.(com|cn|org)', i)
    if res != None:
        print(res.group())
    else:
        print(f'{i}这个网站有错误')

# 高级用法
# 1seacher()：扫描整个字符串并返回第一个成功匹配的对象，如果匹配失败，就返回None
res = re.search('th','python')
print(res.group())

# 2findall()：从头到尾匹配，找到所有匹配成功的数据，返回一个列表
res = re.findall('th','pythonth')
print(res)
print(type(res))

# 3sub(pattern,repl,string,count)
# pattern   正则表达式(代表需要被替换的，也就是字符串里面的内容)
# repl     新内容
# string   字符串
# count   指定替换次数
res = re.sub('bing','b','hellobingbing',count=1)
print(res)
res = re.sub('\\d','2','这是这个月的第30天',count=1)
print(res)

# 4split(pattern,string,maxsplit)
# maxsplit  指定最大分割次数
res = re.split(',','hello,pyhton,123,456')  #未设置次数就全部
print(res)

# 总结：
# match()从头开始匹配，匹配成功返回match对象，通过group进行提取，匹配失败就返回None，只匹配一次
# search()：从头到尾匹配，匹配成功返回第一个成功匹配的对象，通过group进行提取，匹配失败返回None，只匹配一次
# findall()：从头到尾匹配，匹配成功返回一个列表，匹配所有匹配成功的数据，不需要通过group进行提取
# 可看书100页