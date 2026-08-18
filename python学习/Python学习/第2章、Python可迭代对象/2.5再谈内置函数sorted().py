# 列表对象提供了sort()方法支持原地排序，而内置函数sorted()返回新的列表，不对原列表做任何修改
# sorted()函数还可以对元组、字典、集合、字符串等有限长度的可迭代对象排序
from operator import itemgetter

phonebook = [{'name':'Dong','age':37},{'name':'Zhang','age':40},{'name':'Li','age':50},{'name':'Dong','age':43}]
# 使用key来指定排序依据，先按姓名升序排序，姓名相同的按年龄降序排序
print(sorted(phonebook,key=lambda x:(x['name'],-x['age'])))
# 按值排
phonebook = {'Linda':'7704','Bob':'9345','Carol':'5834'}
print(sorted(phonebook.items(),key = itemgetter(1)))
# 按键排
print(sorted(phonebook.items(),key = itemgetter(0)))
# 具体见书58页