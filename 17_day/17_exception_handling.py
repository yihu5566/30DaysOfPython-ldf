# 异常处理
try:
    # 可能出现异常的代码
    result = 10 / 0
except ZeroDivisionError:
    # 处理特定异常
    print("不能除以零")
except Exception as e:
    # 处理其他异常
    print(f"发生错误: {e}")
else:
    # 没有异常时执行
    print(f"结果是: {result}")
finally:
    # 无论是否有异常都会执行
    print("执行完毕")
print('-------------------')
# try:
#     name = input("请输入姓名: ")
#     year = int(input("请输入出生年份: "))
#     age = 2024 - year
#     print(f"{name}的年龄是: {age}")
# except ValueError:
#     print("请输入有效的年份")
# except Exception as e:
    # print(f"发生错误: {e}")

print('-------------------')
# python 中的参数打包和解包
# 我们使用两个运算符：* 和 ** 来实现参数打包和解包
# * 运算符用于打包参数，** 运算符用于打包字典参数
def add(*args): 
    total = 0
    for arg in args:
        total += arg
    return total
# 调用函数
result = add(1, 2, 3, 4, 5)
print(f"结果是: {result}")
print('-------------------')

# def sum_of_five_nums(a, b, c, d, e):
#     return a + b + c + d + e

# lst = [1, 2, 3, 4, 5]
# print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
# 列表解包 
# 使用 range内置函数进行解包
lst = range(1,11) 
print(lst)
print(list(lst))
print('-------------------')
args = [2,8]
nums = range(*args)
print(nums)
print('-------------------')
# 解读字典参数
def unpack_person(**kwargs):
    return f"姓名: {kwargs.get('name')}, 年龄: {kwargs.get('age')}, 性别: {kwargs.get('gender')}"
person_info = {'name': 'Alice', 'age': 30, 'gender': 'Female'}
print(unpack_person(**person_info)) 
print('-------------------')
# 包装
def sum_all(*arges):
    total = 0
    for arg in args:
        total += arg
    return total


print(sum_all(1, 2, 3, 4, 5))
print('-------------------')
# 包装字典
def sum_all(**kwargs):
    for key in kwargs:
        print(f"{key}= {kwargs[key]}")
    return kwargs
print(sum_all(a=1, b=2, c=3))
print('-------------------')
# python 的传播
lst1 = [1, 2, 3]
lst2 = [4,5,6,7, 8, 9]
lst = [0, *lst1, *lst2]
print(lst)
# 枚举
for index, value in enumerate(lst):
    print(f"索引: {index}, 值: {value}")
print('-------------------')
# zip 函数将多个列表打包成一个元组列表
frutis = ['apple', 'banana', 'cherry']
vegetables = ['carrot', 'onion', 'potato']
furit_veg = []
for fruit, veg in zip(frutis, vegetables):
    furit_veg.append({'fruit': fruit, 'vegetable': veg})

print(furit_veg)
print('-------------------')








