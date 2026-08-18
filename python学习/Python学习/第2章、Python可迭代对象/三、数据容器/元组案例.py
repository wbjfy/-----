# 1、计算每个学生的总分、各科平均分，然后一并输出出来
# 2、统计各科成绩的最低分、最高分、平均分，并输出
# 3、查找成绩优秀(平均分大于90)的学生，并输出
students = (
    ('S001','1',85,92,78),
    ('S002','2',92,88,95),
    ('S003','3',78,85,82),
    ('S004','4',88,79,91),
    ('S005','5',95,96,89),
    ('S006','6',76,82,77),
    ('S007','7',89,91,94),
    ('S008','8',75,69,82)
)
for i in students:
    totle = i[2] + i[3] + i[4]
    avg = totle/3
    print(f'{i[0]},{i[1]},总分:{totle},平均分:{avg:.2f}')  #:.2f表示小数取到第2位
# 解包的方式
print()
for a,b,c,d,e in students:
    totle = e + c + d
    avg = totle/3
    print(f'{a},{b},总分:{totle},平均分:{avg:.2f}')
lst1 = [i[2] for i in students]
lst2 = [i[3] for i in students]
lst3 = [i[4] for i in students]

print('最小值：',min(lst1),'\t最大值',max(lst1),'\t平均值',sum(lst1)/len(lst1))
print('最小值：',min(lst2),'\t最大值',max(lst2),'\t平均值',sum(lst2)/len(lst2))
print('最小值：',min(lst3),'\t最大值',max(lst3),'\t平均值',sum(lst3)/len(lst3))
for i in students:
    totle = i[2] + i[3] + i[4]
    avg = totle/3
    if avg > 90:
        print(f'学号：{i[0]}  {avg:.2f}平均分大于90   优秀学生')
print()
# 解包方式
for a,b,c,d,e in students:
    totle = e + c + d
    avg = totle/3
    if avg > 90:
        print(f'学号：{a}  {avg:.2f}平均分大于90   优秀学生')