# 字典的增删改查操作方式:
# 添加   字典名称[key] = value    往指定字典中添加key-value键值对     dict1['王林'] = 688
# 删除   字典名称.pop(key)       删除字典中指定的key，并返回该key对应的value   score = dict1.pop('王林')
#        del 字典名称[key]       删除字典中指定的键值对             del dict1['王林']
# 修改    字典名称[key] = value   修改字典中指定的key对应的值        dict1['王林'] = 688
# 查询    字典名称[key]           根据key获取value                dict1['王林']
#        字典名称.get(key)       根据key获取value                dict1.get('王林')
#        字典名称.keys()          获取所有的key                   dict1.keys()
#        字典名称.values()        获取所有的key                   dict1.values()
#        字典名称.items()         获取所有的kry-value键值对        dict1.items()
dict1 = {'一':1,'二':2,'三':3}
dict1['四'] = 4
print(dict1)
dict1.pop('一')
print(dict1)
del dict1['四']
print(dict1)
dict1['二'] = 20
print(dict1)
print(dict1['二'])
print(dict1.get('三'))
print(dict1.keys())
print(dict1.values())
print(dict1.items())
# 遍历
for k in dict1.keys():
    print(f'{k}: {dict1[k]}')
for item in dict1.items():
    print(f'{item[0]}: {item[1]}')
for k, v in dict1.items():
    print(f'{k}: {v}')