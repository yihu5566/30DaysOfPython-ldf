# 条件语句
a = 3
if a > 2:
    print('a is greater than 2')
else:
    print('a is not greater than 2')

a = 2
if a > 2:
    print('a is greater than 2')
elif a == 2:
    print('a is equal to 2')
else:
    print('a is not greater than 2')
print('-----------------')
# 简写 if-else 语句。 代码 if 条件 else 代码
print('a is greater than 2' if a > 2 else 'a is not greater than 2')
a = -3
print('A是正数') if a > 0 else print('A是负数') # 满足第一个条件，将打印 'A是正数'
# 嵌套 if-else 语句
a = 0
if a > 0:
    print('A是正数')
else:
    if a == 0:
        print('A是零')
    else:
        print('A是负数')

print('-----------------')  
# and 运算符
a = 10
if a > 5 and a < 15:
    print('a is between 5 and 15')
else:
    print('a is not between 5 and 15')
print('-----------------')  
# or 运算符
a = 10
if a > 5 or a < 15:
    print('a is between 5 and 15')
else:
    print('a is not between 5 and 15')
print('-----------------')  
# not 运算符
a = 10
if not (a > 5 and a < 15):
    print('a is not between 5 and 15')


















