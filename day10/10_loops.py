# 循环 循环语句 循环变量 in 循环语句 循环体
count = 0
# 循环语句
while count < 10:
    print(count)
    count += 1
else:
    print('count is not less than 10')
print('-----------------')
# break 语句
count = 0
while count < 10:
    print(count)
    count += 1
    if count == 5:
        break
print('-----------------')
# continue 语句
for i in range(10):
    if i == 5:
        continue
    print(i)
print('-----------------')
# for 循环
numbers = (0, 1, 2, 3, 4, 5)

for i in numbers:
    print(i)
print('-----------------')
# range 函数
# lst = list(range(11)) 
# for i in lst:
#     print(i)
# st  = set(range(1,11)) 
# for i in st:
#     print(i)
# step 参数
step = 2
for i in range(1,11,step):
    print(i)

print('-----------------')
#嵌套循环
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person[key]:
            print(skill)
print('-----------------')
# for 和 else 语句
for i in range(10):
    print(i)
else:
    print('i is not less than 10')
print('-----------------')
# pass 语句
for i in range(6):
    pass
    print(i)
print('-----------------')

















