# 1、从如下数字列表中提取所有偶数，并计算其平方，组成一个新的列表[要插入的值 for i in 序列/列表 if 条件]
s = [2,5,7,2,34,8,345,62,3]
news = [i**2  for i in s if i%2==0]
print(news)
s = [(i+1)**2 for i in range(20)]
print(s)