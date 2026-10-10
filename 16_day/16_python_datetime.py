import datetime
# 日期相关代码
# 获取日期相关数据
print(dir(datetime))  # 查看datetime模块的所有属性和方法
print('-------------------')
now = datetime.datetime.now()  # 获取当前日期时间
print(now)  # 输出当前日期时间
day = now.day  # 获取当前日期的天数
month = now.month  # 获取当前日期的月份
year = now.year  # 获取当前日期的年份
hour = now.hour  # 获取当前时间的小时
minute = now.minute  # 获取当前时间的分钟
second = now.second  # 获取当前时间的秒
microsecond = now.microsecond  # 获取当前时间的微秒
print(f'当前日期时间: {now}, 年: {year}, 月: {month}, 日: {day}, 时: {hour}, 分: {minute}, 秒: {second}, 微秒: {microsecond}')
print('-------------------')
from datetime import datetime
new_year = datetime(2024, 1, 1)  # 创建一个新的日期对象
print(f'新年日期: {new_year}')
day = new_year.day  # 获取新年日期的天数
month = new_year.month  # 获取新年日期的月份
year = new_year.year  # 获取新年日期的年份
hour = new_year.hour  # 获取新年日期的小时
minute = new_year.minute  # 获取新年日期的分钟
print(f'{year}/{month}/{day} {hour}:{minute}')
print('-------------------')
# 使用 strftime() 方法将日期对象格式化为字符串
now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
print(f'格式化后的日期时间: {formatted_date}')
formatted_date = now.strftime('%Y-%m-%d')
print(f'格式化后的日期: {formatted_date}')
formatted_date = now.strftime('%H:%M:%S')
print(f'格式化后的时间: {formatted_date}')
print('-------------------')
# 使用 strptime() 方法将字符串解析为日期对象
date_string = '2024-01-01 12:30:45'
parsed_date = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
print(f'解析后的日期时间: {parsed_date}')
date_string = '5 January, 2024'
parsed_date = datetime.strptime(date_string, '%d %B, %Y')
print(f'解析后的日期: {parsed_date}')
print('-------------------')
from datetime import date

# 使用日期中的日期和时间方法
d = date(2029, 1, 1)
print(f'当前日期: {d.today()}') 
today=date.today()
print(f'当前日期: {today.year}/{today.month}/{today.day}')  # 获取当前日期
print('-------------------')
# 表示时间的物体
from datetime import time
t = time(12, 30, 0)
print(f'当前时间: {t.hour}:{t.minute}:{t.second}')  # 获取当前时间的小时、分钟、秒
print('-------------------')
# 使用两个时间点之间的差异
from datetime import datetime, timedelta, date
today = date(year=2024, month=1, day=1)
new_year = date(year=2025, month=1, day=1)
delta = new_year - today  # 计算两个日期之间的差异
print(f'两个日期之间的差异: {delta.days} 天')  # 输出两个日期之间的天数
t1 = datetime(2019, 1, 1, 0, 59, 0)
t2 = datetime(2020, 1, 1, 0, 0, 0)
delta = t2 - t1  # 计算两个时间点之间的差异
print(f'两个时间点之间的差异: {delta}')  # 输出两个时间点之间的差异
print('-------------------')
# 使用 timedelta 类表示时间差异
t1 = timedelta(weeks=1, days=5, hours=3, minutes=30)  # 创建一个时间差异对象
t2 = timedelta(days=1, hours=2, minutes=15)  # 创建另一个时间差异对象
t3 = t1 - t2  # 计算两个时间差异的差值
print(f'两个时间差异的差值: {t3}')  # 输出两个时间差异的差值











