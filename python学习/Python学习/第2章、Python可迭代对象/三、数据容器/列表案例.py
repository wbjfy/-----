# 1、将用户输入的10个数字，存储到一个列表中，并将列表中的数字进行排序，输出其中的最小值、最大值和平均值
# s = []
# for i in range(10):
#     a = int(input('请输入存入的数字:'))
#     s.append(a)
# s.sort()
# print('最大值：',s[0])
# print('最小值：',s[-1])
# b = 0
# for i in range(10):
#     b += s[i]
# print('平均值：',b/len(s))

# 2、合并两个列表中的元素，并对合并的结果进行去重处理（去除列表中的重复元素）
# s1 = [1,2,3,4]
# s2 = [4,6,7,8]
# for i in s2:
#     s1.append(i)
# print(s1)
# news = []
# for i in s1:
#     # 元素去重
#     if i not in news:
#         news.append(i)
# print(news)

# 解包：将列表这一类容器解开成一个一个独立的元素
# 组包：将多个值合并到一个容器
# a = [1,2,3,4,4,5]
# b = [5,6,7]
# news1 = [*a,*b]
# news2 = a + b
# print(news1)
# print(news2)

# 3、生成1-20的平方列表
# 传统方式
# s = []
# for i in range(1,21):
#     s.append(i**2)
# print(s)
# 简单方式：列表推导式
# s = [(i+1)**2 for i in range(20)]
# print(s)

# 4、从如下数字列表中提取所有偶数，并计算其平方，组成一个新的列表[要插入的值 for i in 序列/列表 if 条件]
s = [2,5,7,2,34,8,345,62,3]
news = [i**2  for i in s if i%2==0]
print(news)