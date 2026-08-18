import re
# 贪婪与非贪婪
# 1贪婪匹配(默认)：在满足匹配时，匹配尽可能长的字符串
res = re.match('em*','emmmmmm....')
print(res.group())

# 2非贪婪匹配：在满足匹配时，匹配尽可能短的字符串，使用?来表示
res = re.match('em*?','emmmmmm....')
print(res.group())

# 原生字符串
# python中字符串前加上r表示原生字符串
print(r'sixs\tar')   #取消转义
res = re.match(r'\\\\',r'\\game')
print(res.group())
#正则表达式中，匹配字符串中的字符\需要\\\\,加入原生字符串，\\代表\

