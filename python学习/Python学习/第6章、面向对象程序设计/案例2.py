# 采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能
# 系统使用自定义对象存储商品数据,通过控制台菜单与用户交互具体功能如下:
# 1、添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车
# 2、修改购物车:要求用户输入要修改的购物车商品名称，让后再提示输入该商品的价格、数量，输入完成后修改该商品信息
# 3、删除购物车:将购物车中的商品信息展示出来，格式为:"商品名称: xxx，商品价格: xxx，商品数量:xxx"
# 4、查询购物车:将购物车中的商品信息展示出来
# 5、退出购物车
# 购物车类
from platform import system


class Shop:
    def __init__(self,name,num,cost):
        self.name = name
        self.num = num
        self.cost = cost
    def __str__(self):
        return f'商品名称:{self.name} | 商品数量:{self.num} | 商品价格{self.cost}'
    def update_shop(self,num = None,cost = None):
        if num is not None:
            self.num = num
        if cost is not None:
            self.cost = cost
#购物车系统类
class EduManagement:
    system_version = '1.0'
    def __init__(self):
        self.shop_list = []
# 1、添加购物车
    def add_shop(self):
        name = input("请输入商品名称:")
        for s in self.shop_list:
            if s.name == name:
                print('已添加过该商品')
                return
        num = int(input('请输入该商品数量:'))
        cost = int(input('请输入该商品价格:'))
        stu = Shop(name,num,cost)
        self.shop_list.append(stu)
        print('添加成功')

# 2、修改购物车
    def update_shop(self):
        name = input("请输入要修改的商品名称:")
        for s in self.shop_list:
            if s.name == name:
                num = int(input('请输入修改后该商品数量:'))
                cost = int(input('请输入修改后该商品价格:'))
                s.update_shop(num,cost)
                print('修改成功')
                return
        print('未找到该商品修改失败')

# 3、删除购物车
    def delete_shop(self):
        name = input("请输入要删除的商品名称:")
        for s in self.shop_list:
            if s.name == name:
                self.shop_list.remove(s)
                print('删除成功')
                return
        print('未找到该商品删除失败')

# 4、查询购物车
    def show_shop(self):
        for s in self.shop_list:
            print(s)
# 运行系统方法
    def run(self):
        print(f'欢迎使用购物车系统  V{EduManagement.system_version}')
        while True:
            print('''
            ################################################################
            1、添加购物车  2、修改购物车  3、删除购物车  4、查询购物车  5、推出购物车系统
            ################################################################''')
            print()
            choice = input('请输入要执行的操作，输入1-5:')
            match choice:
                case '1':
                    self.add_shop()
                case '2':
                    self.update_shop()
                case '3':
                    self.delete_shop()
                case '4':
                    self.show_shop()
                case '5':
                    print('bye')
                    break
                case _:
                    print('请规范操作')

if __name__ == '__main__':
    edu_management = EduManagement()
    edu_management.run()