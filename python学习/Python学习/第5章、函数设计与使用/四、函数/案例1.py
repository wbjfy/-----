# 1、定义一个函数:根据传入的底和高计算三角形面积的函数(三角形面积 = 低 * 高 / 2).
def a(d,h):
    """
    根据传入计算三角形面积
    :param d: 底
    :param h: 高
    :return: 面积
    """
    return d * h / 2
print(f'底为30，高为20的三角形面积:{a(30, 20)}')
# 2、定义一个函数:自诉案传入的字符串中元音字母的个数(元音字母为aeiouAEIOU)。
def b(s):
    """
    统计字符串中元音字母的个数
    :param s: 传入字符串
    :return: 个数
    """
    num = 0
    for i in s:
        if i in 'aeiouAEIOU':
            num += 1
    return num
print(b('hello python hello world'))
# 3、定义一个函数:计算传入的把你学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数)，并返回
def c(list1):
    """
    计算传入班级同学成绩的最高分最低分和平均值
    :param list1: 传入成绩
    :return: 最高分，最低分，平均值
    """
    max_ = max(list1)
    min_ = min(list1)
    avg = sum(list1) / len(list1)
    return max_, min_, round(avg,1)
lst1 = [589,609,605,643,677,455,477,489,503]
print(c(lst1))
