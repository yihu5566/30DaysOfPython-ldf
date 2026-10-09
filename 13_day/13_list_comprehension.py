# 列表推导式
# 语法：[表达式 for 变量 in 可迭代对象 if 条件]
# 示例：[x for x in range(1, 10) if x % 2 == 0]
even_numbers = [x for x in range(1, 10) if x % 2 == 0]
print(even_numbers)

# 将字符串转化为列表
string = "Python"
char_list = [char for char in string]
print(char_list)
print("--------------------------------------------------")
# 将列表中的每个元素平方
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)
# 元组推导式
tuple_of_squares = tuple([(x, x**2) for x in numbers])
print(tuple_of_squares)
print("--------------------------------------------------")
# 推导式和if结合
numbers = [i for i in range(1, 21)]
# 过滤出偶数
even_squares = [x for x in numbers if x % 2 == 0]
print(even_squares)
print("--------------------------------------------------")
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
# 过滤出大于 0 的 偶数
even_numbers = [x for x in numbers if x > 0 and x % 2 == 0]
print(even_numbers)
print("--------------------------------------------------")
# 扁平三维数组
three_d_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in three_d_array for num in row]
print(flattened)
print("--------------------------------------------------")
# lambda 表达式
# 语法：lambda 变量1, 变量2, ...: 表达式
# 示例：lambda x: x**2
square = lambda x: x**2
print(square(5))
print("--------------------------------------------------")
def add_tow_numbers(x, y):
   return x + y
print(add_tow_numbers(3, 5))
add_tow_numbers_lambda = lambda x, y: x + y
print(add_tow_numbers_lambda(3, 5))
# 自调用lambda表达式
print((lambda x, y: x + y)(3, 5))
# 多变量
print((lambda x, y, z: x + y + z)(3, 5, 7))
print("--------------------------------------------------")
# lambda 在另一个函数中使用
def power(x):
    return lambda n: x ** n

cube = power(2)(3)
print(cube)

cube_function = power(2)(5)
print(cube_function)






















