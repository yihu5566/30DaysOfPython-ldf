# 函数 语法

# 声明函数
def function_name():
    # 函数体
    print("hello world")

# 调用
function_name()

# 生成名字 返回值
def generate_name():
    first_name = "小"
    last_name = "明"
    return first_name + last_name

# 调用生成名字的函数
name = generate_name()
print(name)

# 参数函数
def add(a, b):
    return a + b

# 调用加法函数
result = add(3, 5)
print(result)
# 简直对传参数

def function_with_default_param(a, b):
    # 函数体
    print(a + b)
function_with_default_param(a=3, b=5)  # 输出 8
# 带返回值的函数
def function_with_return(a, b):
    # 函数体
    return a + b
# 调用带返回值的函数
result = function_with_return(a=3, b=5)
print(result)
print("-----------------") 
# 带默认参数的函数
def greet(b='alice'):
    # 函数体
    print( b, "你好")
greet()  # 输出 alice 你好
greet(b='bob')  # 输出 bob 你好
print("-----------------")
# 带可变参数的函数
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
# 调用带可变参数的函数
result = sum_numbers(1, 2, 3, 4, 5)
print(result)  # 输出 15
print("-----------------")
# 函数默认和不定量参数
def generate_groups(a, *args):
    print("a:", a)
    for arg in args:
        print("arg:", arg)

# 调用函数
generate_groups(1, 2, 3, 4)
print("-----------------")
# 作为另一个函数的参数
def square(a):
    return a ** 2

def dosomething(func, value):
    return func(value)

# 调用函数
result = dosomething(square, 3)
print(result)  # 输出 9
print("-----------------")






