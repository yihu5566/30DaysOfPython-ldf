# 字符串
print('-----------------')
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters)
print(len(letters))
#  多行字符串
print('-----------------')
multi_line_str = '''
I am a student.
I am a student.
'''
print(multi_line_str)

multi_line_str = """
I am a student.
I am a student.
"""
print(multi_line_str)
print('-----------------')

first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name + space + last_name
print(full_name)
# 字符串转译
print('-----------------')
print('I am a student.\nI am a student.')
print('Days\tTopics\tExercises') # 增加一个制表符
print('Day 1\t3\t5')
print('Day 2\t3\t5')

print('this is a backslash  symbol (\\)') # 输出一个反斜杠
# 单引号中用双引号
print('He said, \"Python is awesome.\"') # 输出双引号
# 字符串格式化
print('-----------------')
first_name = 'Asabeneh'
last_name = 'Yetayeh'
format_string = 'Hello, %s %s!' % (first_name, last_name)
print(format_string)

radius = 10
pi = 3.14
area = pi * radius ** 2
print('Area of a circle with radius %d is %.2f' % (radius, area))

python_libraries = ['Django', 'Flask', 'NumPy', 'Pandas', 'Matplotlib', 'Tkinter']
print('I use %s library in my project.' % (python_libraries))

# 新字符串格式化方法
print('-----------------')
format_string = 'Hello, {} {}!'.format(first_name, last_name)
print(format_string)

a = 4 
b = 3
print('{} + {} = {}'.format(a, b, a+b))
print('{} - {} = {}'.format(a, b, a-b))
print('{} * {} = {}'.format(a, b, a*b))
print('{} / {} = {:.2f}'.format(a, b, a/b))

# 字符串插值
print('-----------------')
print(f'Hello, {first_name} {last_name}!')
print(f'{a} + {b} = {a+b}')

# 字符串序列
language = 'Python'
print(language[0]) # P
a,b,c,d,e,f = language
print(a) # P
# 字符串切片
print('-----------------')
print(language[0:3]) # Pyt
print(language[3:6]) # hon
print(language[-3:]) # hon
print(language[3:]) # hon
# 字符串反转
print('-----------------')
print(language[::-1]) # nohtyP
# 切片时跳过字符
print(language[0:6:2]) # Pto

print('-----------------')
# 字符串方法
challennge = 'thirty days of python'
print(challennge.upper()) # THIRTY DAYS OF PYTHON
print(challennge.lower()) # thirty days of python
print(challennge.capitalize()) # Thirty days of python
print(challennge.count('y')) # 3
print(challennge.count('y',7,14)) # 1

print(challennge.endswith('on')) # True
print(challennge.endswith('thirty')) # False
print('------------------')
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs()) # thirty  days    of      python
print(challenge.expandtabs(12)) # thirty    days      of        python
print('------------------')
challenge = 'thirty days of python'
print(challenge.find('y')) 
print(challenge.rfind('y')) 
print(challenge.index('y')) 
# print(challenge.rindex('da',9))  # ValueError: substring not found
print('------------------')
print(challenge.isalnum()) # False
challenge = 'thirtydaysofpython'
print(challenge.isalnum()) # True
print(challenge.isalpha()) # True
challenge = '30DaysPython'
print(challenge.isalnum()) # True
print(challenge.isalpha()) # False
print('------------------')
challenge = 'thirty days of python'
print(challenge.isdigit()) # false
challenge = '30'    
print(challenge.isdigit()) # True
print('------------------')
num = '22'
print(num.isnumeric()) # True
num='10.5'
print(num.isnumeric()) # False
num='\u00B2'  # Unicode for squared symbol
print(num.isnumeric()) # True

print('------------------')
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, 因为以数字开头
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True
print('------------------')
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False
print('------------------')
challenge = 'thirty days of python'
print(challenge.isupper()) # False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True
# join 方法
print('-----------------')
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # HTML CSS JavaScript React
result = '# '.join(web_tech)
print(result) # HTML# CSS# JavaScript# React
print('-----------------')
challenge = 'thirty days of pythoon'
print(challenge.strip('noth')) # thirty days of pyth
print('-----------------')
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # thirty days of coding
print('-----------------')
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']
print('-----------------')  
print(challenge.title()) # Thirty Days Of Python
print('-----------------')
challenge = 'thirty days of python'
print(challenge.swapcase()) # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase()) # tHIRTY dAYS oF pYTHON
print('-----------------')
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True
print(challenge.startswith('thirty days')) # True
challenge = '30 days of python 2020'
print(challenge.startswith('thirty')) # False











