# 根据提供的班级学生的选课情况，完成如下需求：
# 1、找出同时选修了法语和艺术的学生
# 2、找出同时选修了所有四门课程的学生
# 3、找出选修了足球，但是没有选修篮球的学生
# 4、统计每个学生选修的课程数量
# 选修足球学生的名单
football_set={"王林","曾牛","徐立国","遁天","天运子","韩立","厉飞雨","乌丑","紫灵"}
# 选修篮球学生名单
basketball_set={"张铁","墨居仁","王林","姜老道","曾牛","王蝉","韩立","天运子","李化元","厉飞雨","云露"}
# 选修法语名单
french_set={"许木","王卓","十三","虎咆","姜老道","天运子","红蝶","厉飞雨","韩立","曾牛"}
# 选修艺术学生名单
art_set={"遁天","天运子","韩立","虎咆","姜老道","紫灵"}
# 方式一
print('同时选修了法语和艺术的学生:',end = ' ')
print(french_set.intersection(art_set))
# 方式二  & --> 取交集
print(french_set & art_set)
print('同时选修了四门课程的学生:',end = ' ')
print(football_set.intersection(basketball_set).intersection(french_set).intersection(art_set))
print(football_set & basketball_set & art_set & french_set)
# 方式一
print('选修了足球但未选修篮球的学生:',end=' ')
print(football_set.difference(basketball_set))
# 方式二  - -->差集
print(football_set - basketball_set)
# 方式三  集合推导式--> 快速构建集合，语法: {要往集合中添加的数据 for s in set1 if 条件}
print({s for s in football_set if s not in basketball_set})
print('统计每个学生选修的课程数量:',end=' ')
# 第一步获取学生名单  | --> 并集
all_set = football_set | basketball_set | art_set | french_set
all_list = [*football_set,*basketball_set,*art_set,*french_set]
for s in all_set:
    print(f'{s}选修了{all_list.count(s)}门课')