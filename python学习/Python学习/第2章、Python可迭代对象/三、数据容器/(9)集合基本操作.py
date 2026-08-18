# 场景：在业务中，需要定义一个变量，来批量存储用户的手机号（唯一的）
# 列表list、元组tuple可以存吗？   不可以，因为这两种类型是可以存储重复元素的
# 此时就可以使用集合set来存储，set会自动去重，存储不重复的元素
# 介绍：集合（set）是一种无序的、不可重复的、可修改的数据容器。
# 定义：
s1 = {1,2,3,4,5,5}
print(s1)
# 定义空集合
s2 = set()
# 注意：空集合的定义不可以使用{},{}表示的是空字典；由于集合是无序的，因此是不支持下标索引访问的
# add()         添加元素到集合中                         s1.add('t')
# remove()      移除集合中的指定元素(指定元素不存在将报错)    s1.remove('t')
# pop()         随机删除集合中的元素并返回                 e = s1.pop()
# clear()       清空集合                               s1.clear()
# difference()  求取两个集合的差集(包含在第一个但不包含在第二个集合的元素)  s1.difference(s2)
# union()       求取两个集合的并集                       s1.union(s2)
# intersection() 求取两个集合的交集                      s1.intersection(s2)
a = {1,2,3,4,5,6}
a.add(7)
print(a)
a.remove(7)
print(a)
a.pop()
print(a)
a.clear()
print(a)
a = {1,2,3,4}
b = {2,4,6,8}
c = a.difference(b)
print(c)
c = a.union(b)
print(c)
c = a.intersection(b)
print(c)