# 字典 dict 是一种无序的、可变的、可重复的集合
empty_dict = {}
empty_dict = dict()
# 字典的键值对
dict1 = {'name': 'ludongfang', 'age': 20, 'gender': 'male'}
print(dict1)
print(dict1['name'])
print(dict1['age'])
print(dict1['gender'])

# 字典的嵌套
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
} 
print(person['first_name'])
print(person.get('first_name'))

# add key-value pair
person['city'] = 'Helsinki'
print(person)
# update key-value pair
person['age'] = 251
print(person)
print('---------------------')
# check if a key exists
print('city' in person)
# del key-value pair
del person['city']
person.pop('age')
person.popitem()
print(person)
print('---------------------')
# change dict to list
print(person.items())
print(list(person.items()))
print('---------------------')
# 语法：dict.clear()
# 说明：清空字典，删除所有键值对
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# print(dct.clear()) # None
# delete dict
# del dct
# print(dct) # NameError: name 'dct' is not defined
# copy dict
dct2 = dct.copy()
print(dct2)
# 语法：dict.keys()
# 说明：合并字典的键值对，返回一个视图对象
print(dct.keys())
# 语法：dict.values()
# 说明：合并字典的键值对，返回一个视图对象
print(dct.values())
print(list(dct.values())[0])















