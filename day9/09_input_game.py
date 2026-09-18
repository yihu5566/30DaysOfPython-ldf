age = input('What is your age? ')
age = int(age)

if age >= 18:
    print('You are an adult')
else:
    age_diff = 18 - age
    print(f'You are a minor, 你还差 {age_diff} 岁成年')

