# 获取高分电影榜单(Top100)数据，并保存在csv文件中
# 数据包括:电影名、年份、上映时间、类型、时长、评分、语言、导演、作者、主演、Slogan、简介。
# csv:(Comma-Separated Values,逗号分隔值)，是一种简单、通用的文本文件格式，用于存储表格数据，可以直接使用Excel打开
# csv操作 - 方式一：
# 写
with open("csv_data/01.csv","w",encoding="utf-8") as f:
    f.write("姓名,年龄,性别,爱好\n") #写入表头
    f.write("小王,18,男,'football,Java'\n") #写入数据
    f.write("小李,19,女,write")

# 读
with open("csv_data/01.csv","r",encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# csv操作 - 方式二：
import csv
with open("csv_data/02.csv","w",encoding="utf-8",newline='') as f:
    writer = csv.DictWriter(f,fieldnames=["姓名","年龄","性别","爱好"])
    writer.writeheader() #写入表头
    writer.writerow({"姓名":"小王","年龄":"18","性别":"男","爱好":"football"})

# 读
with open("csv_data/02.csv","r",encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)