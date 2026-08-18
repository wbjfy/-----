# 要求：
# 1、添加学生信息:根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
# 2、修改学生信息:要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
# 3、删除学生信息:要求输入要删除的学生姓名，根据姓名删除学生信息。
# 4、查询学生信息:要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
# 5、列出所有学生:遍历所有学生信息并输出。
# 6、统计班级成绩:统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名
# 7、退出系统
contrul_dict = {}
while True:
    print("""
    ########## 教务管理系统 ##########
    #        1.添加学生信息          #
    #        2.修改学生信息          #
    #        3.删除学生信息          #
    #        4.查询学生信息          #
    #        5.列出所有学生          #
    #        6.统计班级成绩          #
    #        7.退出系统             #""")
    choice = input("请输入要执行的操作(1-7)")
    match choice:
        case '1':
            students_name = input('请输入学生姓名: ')
            if students_name in contrul_dict:
                print("该学生已存在，请重新选择")
                continue
            students_chinese = float(input('请输入学生语文成绩: '))
            students_math = float(input('请输入学生数学成绩: '))
            students_english = float(input('请输入学生英语成绩: '))
            contrul_dict[students_name] = {'chinese':students_chinese, 'math':students_math, 'english':students_english}
            print('学生添加完毕')
        case '2':
            students_name = input('请输入要修改的学生的姓名: ')
            if students_name not in contrul_dict:
                print('该学生不存在，请重新选择')
                continue
            students_chinese = float(input('请输入学生新的语文成绩: '))
            students_math = float(input('请输入学生新的数学成绩: '))
            students_english = float(input('请输入学生新的英语成绩: '))
            contrul_dict[students_name] = {'chinese':students_chinese, 'math':students_math, 'english':students_english}
            print('修改成功')
        case '3':
            students_name = input('请输入要删除的学生的姓名')
            if students_name not in contrul_dict:
                print('该学生不存在，请重新选择')
                continue
            del contrul_dict[students_name]
            print('删除成功')
        case '4':
            students_name = input('请输入要查询的学生的姓名')
            if students_name not in contrul_dict:
                print('该学生不存在，请重新操作')
                continue
            print(f'姓名:{students_name},语文成绩:{contrul_dict[students_name]['chinese']},数学成绩:{contrul_dict[students_name]['math']},英语成绩:{contrul_dict[students_name]['english']}')
        case '5':
            for students_name in contrul_dict.keys():
                print(f'姓名:{students_name},语文成绩:{contrul_dict[students_name]['chinese']},数学成绩:{contrul_dict[students_name]['math']},英语成绩:{contrul_dict[students_name]['english']}')
        case '6':
            list1 = [i['chinese'] for i in contrul_dict.values()]
            list2 = [i['math'] for i in contrul_dict.values()]
            list3 = [i['english'] for i in contrul_dict.values()]
            print(f'语文最高分:{max(list1)},\t姓名：{[i for i in contrul_dict.keys() if max(list1) == contrul_dict[i]['chinese']]},\t最低分:{min(list1)},\t姓名:{[i for i in contrul_dict.keys() if min(list1) == contrul_dict[i]['chinese']]}')
            print(f'数学最高分:{max(list2)},\t姓名：{[i for i in contrul_dict.keys() if max(list2) == contrul_dict[i]['math']]},\t最低分:{min(list2)},\t姓名:{[i for i in contrul_dict.keys() if min(list2) == contrul_dict[i]['math']]}')
            print(f'英语最高分:{max(list3)},\t姓名：{[i for i in contrul_dict.keys() if max(list3) == contrul_dict[i]['english']]},\t最低分:{min(list3)},\t姓名:{[i for i in contrul_dict.keys() if min(list3) == contrul_dict[i]['english']]}')
            print(f'语文平均值:{sum(list1)/len(list1)},\t数学平均值:{sum(list2)/len(list2)},\t英语平均值:{sum(list3)/len(list3)}')
        case '7':
            print('成功退出')
            break
        case _:
            print('非法操作,不支持!!!')