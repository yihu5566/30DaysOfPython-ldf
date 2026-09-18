import mymodule as mm
print(mm.generate_full_name("ludongfang", "li"))
print(mm.sum_numbers(3, 5))

print("--------------------------------------------------")
from mymodule import generate_full_name, sum_numbers
print(generate_full_name("ludongfang", "li"))
print(sum_numbers(3, 5))

# 倒入内置模块
import os
print(os.getcwd())
print(os.listdir())
print("--------------------------------------------------")
# 倒入内置模块 sys  读取传入的参数
import sys
# print('welcome {}. enjoy {} challenge'.format(sys.argv[1], sys.argv[2]))
print("--------------------------------------------------")
# 统计模块
import statistics
print(statistics.mean([1, 2, 3, 4, 5]))
print(statistics.median([1, 2, 3, 4, 5]))
print(statistics.mode([1, 2, 3, 4, 5]))
print(statistics.stdev([1, 2, 3, 4, 5]))

print("--------------------------------------------------")
# 数学模块
import math
print(math.pi)           # 3.141592653589793, pi 常数
print(math.sqrt(2))      # 1.4142135623730951, 平方根
print(math.pow(2, 3))    # 8.0, 指数函数
print(math.floor(9.81))  # 9, 向下取整
print(math.ceil(9.81))   # 10, 向上取整
print(math.log10(100))   # 2, 以 10 为底的对数

print("--------------------------------------------------")
# 字符串模块
import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
print(string.whitespace)
print('--------------------------------------------------')
# 倒入随机数
from random import randint, random
print(randint(1, 10))
print(random())













