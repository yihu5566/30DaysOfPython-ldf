# 类型错误

# 语法错误 SyntaxError 例如，缺少冒号
try:
    def add(a, b):
        return a + b
except SyntaxError:
    print('缺少冒号')
print('-------------------')
# NameError: 未定义的变量
# 例如，尝试访问未定义的变量
try:
    print(x)
except NameError:
    print('变量未定义')
print('-------------------')
# ValueError: 无效的值
# 例如，尝试将非数字字符串转换为整数    
try:
    num = int('12v')
except ValueError:
    print('转换失败')
print('-------------------')
# IndexError: 列表索引超出范围
# 例如，尝试访问列表中不存在的索引
my_list = [1, 2, 3] 
try:
    print(my_list[3])
except IndexError:
    print('索引超出范围')
print('-------------------')
# ModuleNotFoundError: 模块未找到
# 例如，尝试导入不存在的模块
try:
    import non_existing_module
except ModuleNotFoundError:
    print('模块未找到')
print('-------------------')
# 属性错误
# 例如，尝试访问不存在的属性
class MyClass:
    def __init__(self):
        self.name = 'MyClass'
my_class = MyClass()
try:
    print(my_class.age)
except AttributeError:
    print('属性不存在')
print('-------------------')
# KeyError: 字典中不存在的键
# 例如，尝试访问字典中不存在的键    
my_dict = {'a': 1, 'b': 2}
try:
    print(my_dict['c'])
except KeyError:
    print('键不存在')
print('-------------------')
# TypeError: 不支持的类型操作
# 例如，尝试对字符串进行加法操作
a = '1'
b = 2
try:
    print(a + b)
except TypeError:
    print('类型错误')
print('-------------------')
# ZeroDivisionError: 除以零错误
# 例如，尝试将一个数除以零
try:
    result = 10 / 0
except ZeroDivisionError:
    print('除以零错误')

print('-------------------')
# ImportError: 导入错误
# 例如，尝试从模块中导入不存在的函数
try:
    from math import non_existing_function
except ImportError: 
    print('导入错误')
print('-------------------')
