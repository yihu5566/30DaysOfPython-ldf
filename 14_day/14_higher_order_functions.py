# 高阶函数
# 函数作为参数
# 函数作为返回值
# 函数作为元素

def sum_numbers(nums):
    return sum(nums)  # 计算列表中所有元素的和

def higher_order_function(func, nums):
    sum_result = func(nums)  # 调函数并返回结果
    return sum_result  # 返回函数调用结果

result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)  # 输出: 15


# 函数作为返回值
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    return abs(x)

def higher_order_function(type): #将函数作为返回值，根据type返回不同的函数
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute
    else:
        return None

 # 调用返回的函数
func = higher_order_function('square')
print(func(3))  # 输出: 9
func = higher_order_function('cube')
print(func(3))  # 输出: 27
func = higher_order_function('absolute')
print(func(-10))  # 输出:: 10    

print('-------------------')
# 闭包是指在函数内部定义的函数，该函数可以访问外部函数的变量
# 闭包作用：封装状态和行为
# 闭包可以实现状态的隐藏和保护，同时提供状态的访问和修改； 
# 让函数内部的变量不被外部直接访问，从而实现数据的封装和保护。

def create_counter():
    count = 0
    # 定义一个内部函数，该函数可以访问外部函数的变量count
    def counter():
        nonlocal count
        count += 1
        return count
    # 返回内部函数
    return counter
counter = create_counter()  # 创建一个计数器
print(counter())  # 输出: 1
print('-------------------')
# python装饰器 是一种在函数定义前添加额外功能的机制
# 装饰器可以用于日志记录、权限检查、性能测试等场景
def greeting():
    print('Hello, World!')

def decorator(func):
    def wrapper():
        print('Before calling the function')
        func()  # 调用被装饰的函数
        print('After calling the function')
    return wrapper
greeting = decorator(greeting)  # 装饰器装饰greeting函数
# 调用装饰后的greeting函数
greeting()  # 输出: Before calling the function Hello, World! After calling the function
# 通过注解装饰greeting函数
@decorator
def greeting():
    print('Hello, World!')
# 调用装饰后的greeting函数
greeting()  # 输出: Before calling the function Hello, World! After calling the function
print('-------------------')
# 装饰器可以用于多个函数，每个函数都可以独立装饰，互不干扰.
# 第一个装饰 字符转大写
def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper
# 第二个装饰 字符拆分
def split_string(func):
    def wrapper():
        split_result = func().split()
        return split_result
    return wrapper
# 通过注解装饰greeting函数
@split_string
@uppercase
def greeting():
    return 'Hello, World!'
# 调用装饰后的greeting函数
print(greeting())
print('-------------------')
# 装饰器可以带参数
def decorator_with_argument(fun):
    def wrapper_accepting_arguments(*args):
       fun(*args)
       print(f'i live in {args[0]}')
    return wrapper_accepting_arguments

def print_full_name(first, last,city):
    print(f'My name is {first} {last}')

print_full_name = decorator_with_argument(print_full_name)
print_full_name('John', 'Doe','New York')
print('-------------------')
# 内置高阶函数
# map() 函数接收两个参数，一个是函数，一个是可迭代
# map(func, iterable)

nums = [1, 2, 3, 4, 5]
# 使用map函数将列表中的每个元素平方
squared_nums = list(map(lambda x: x ** 2, nums))
print(squared_nums)  # 输出: [1, 4, 9, 16, 25]
print('-------------------')

# 字符列表转整数
nums = ['1', '2', '3', '4', '5']
int_nums = list(map(int, nums))
print(int_nums)  # 输出: [1, 2, 3, 4, 5]
print('-------------------')
# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象
# filter(func, iterable)
# 使用filter函数过滤出列表中的偶数
nums = [1, 2, 3, 4, 5, 6]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)  # 输出: [2, 4, 6]
print('-------------------')
# reduce() 函数用于对序列进行累积操作，返回一个值
# reduce(func, iterable)
from functools import reduce
# 使用reduce函数计算列表中所有元素的和
nums = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, nums)
print(result)  # 输出: 15
print('-------------------')

















