# 列表 List 操作
lst = list()
empty_lst = list()
print(lst, empty_lst)  # 输出两个空列表
print('------------------------')
# 列表的创建
fruits = ['apple', 'banana', 'orange']
print(fruits)  # 输出列表
vegetables = ['carrot', 'onion', 'potato']
print(vegetables)  # 输出列表
web_tech = ['html', 'css', 'js']
print(web_tech)  # 输出列表
countries = ['china', 'usa', 'japan']
print(countries)  # 输出列表
print(countries[0])  # 输出列表的第一个元素，即 china
print(len(countries))  # 输出列表的长度，即 3
print('------------------------')
# 列表可以存储不同数据类型的元素
mixed_lst = [1, 2.3, 'Asabeneh', True, None]
print(mixed_lst)  # 输出列表
print(type(mixed_lst))  # 输出列表的类型，即 list
# 负索引
print(mixed_lst[-1])  # 输出列表的最后一个元素，即 None
print('------------------------')
# 拆解列表
first, second, third, *rest = mixed_lst
print(first, second, third)  # 输出 1 2.3 Asabeneh
print(rest)  # 输出 [True, None]
print('------------------------')
# 列表切分
fruits = ['apple', 'banana', 'orange', 'peach']
all_fruits = fruits[0:4]
print(all_fruits)  # 输出 ['apple', 'banana', 'orange', 'peach']
print(fruits[0:])  # 输出 ['apple', 'banana', 'orange', 'peach']
print(fruits[::2])  # 输出 ['apple', 'orange']
print('------------------------')
# 负数索引
print(fruits[-1])  # 输出 'peach'
print(fruits[-2:])  # 输出 ['orange', 'peach']
print(fruits[-3:-1])  # 输出 ['banana', 'orange']
print(fruits[::-2])  # 输出 ['peach', 'banana']
print('------------------------')
# 列表修改
fruits = ['apple', 'banana', 'orange', 'peach']
fruits[0] = 'blackcurr'
print(fruits)  # 输出 ['blackcurr', 'banana', 'orange', 'peach']
print('------------------------')
# 列表添加元素
fruits.append('watermelon')
print(fruits)  # 输出 ['blackcurr', 'banana', 'orange', 'peach', 'watermelon']
fruits.insert(2, 'lemon')
print(fruits)  # 输出 ['blackcurr', 'banana', 'lemon', 'orange', 'peach', 'watermelon']
print('------------------------')
# 列表删除元素
fruits.remove('orange')
print(fruits)  # 输出 ['blackcurr', 'banana', 'peach', 'watermelon']
print('------------------------')
fruits.pop(2)
print('pop删除peach后:',fruits)
print('------------------------')
# 列表清空
fruits.clear()
print(fruits)  # 输出 []
print('------------------------')
# 列表复制
fruits = ['apple', 'banana', 'orange', 'peach']
fruits_copy = fruits.copy()
print(fruits_copy)  # 输出 ['apple', 'banana', 'orange', 'peach']
print('------------------------')
does_exist = 'orange' in fruits_copy
print(does_exist)  # 输出 True  
print('------------------------')
# del 删除元素
fruits_copy = ['blackcurr', 'banana', 'peach', 'watermelon']
del fruits_copy[2]
print(fruits_copy)  # 输出 ['blackcurr', 'banana', 'watermelon']
print('------------------------')
# 链接列表
positive_ints = [1, 2, 3, 4, 5]
zero = [0]
negative_ints = [-5, -4, -3, -2, -1]
print(positive_ints + zero + negative_ints)  # 输出 [1, 2, 3, 4, 5, 0, -5, -4, -3, -2, -1]
print('------------------------')
# 语法
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)
print(list1)  # 输出 ['item1', 'item2', 'item3', 'item4', 'item5']
print('------------------------')
# 统计列表项
print(list1.count('item3'))  # 输出 1
print('item3的索引为:',list1.index('item3'))
print('------------------------')
# 列表反转
list1.reverse()
print('反转后的列表:',list1)  # 输出 ['item5', 'item4', 'item3', 'item2', 'item1']
print('------------------------')
# 列表排序
list1.sort()
print('排序后的列表:',list1)  # 输出 ['item1', 'item2', 'item3', 'item4', 'item5']
list1.sort(reverse=True)
print('反向排序后的列表:',list1)  # 输出 ['item5', 'item4', 'item3', 'item2', 'item1']
print('------------------------')










