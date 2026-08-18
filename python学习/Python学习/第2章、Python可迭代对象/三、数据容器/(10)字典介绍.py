# python中的字典(dict)，里面存储的是键值对(key:value)类型的数据，可以根据键(key)找到对应的值(value)
# 特点：键值对(key:value)存储、键(key)不能重复、可修改
# 定义字典存储
dict1 = {'王林':670,'韩立':556}
# 定义空字典
# 字典名称 = {}
# 字典名称 = dict()
# 根据key获取value
# 值 = 字典名称[key]
# 注意：字典(dict)中的value可以是任何类型的数据，而key不能为可变类型(如不可变类型：列表list、集合set、字典dict)
# key(可以为 str、int、float、tuple)
# 访问
print(dict1['王林'])
# 修改
dict1['王林'] = 888
print(dict1)