# 1、邮箱格式验证：用户输入一个邮箱，验证邮箱格式是否正确（包含一个@和至少一个.）。
str1 = input("请输入邮箱")
if str1.find('@') == 1 and str1.find('.') >= 1:
    print('格式正确')
else:
    print('格式错误')