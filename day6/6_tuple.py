# 元组 tuple
# 元组是一种不可变的序列类型，元组中的元素是有序的，但是元组中的元素是不可变的
# 元组的元素可以是任意类型，包括数字、字符串、元组等

empty_tuple = ()
empty_tuple = tuple()

tpl = ('item1', 'item2', 'item3')
print(tpl)
print(len(tpl))
print(tpl[0])
print(tpl[len(tpl)-1])
# 元组切片
print(tpl[0:2])
print(tpl[1:])
# 负索引
print(tpl[-1])
# 检查元组的元素是否存在
print('item2' in tpl)
print('item4' in tpl)
# 链接元组
tpl2 = ('item4', 'item5', 'item6')
print(tpl2)
print(tpl + tpl2)
# 删除元组 删除后不能使用，报错：NameError: name 'tpl' is not defined. Did you mean: 'tpl2'?
del tpl 
print(len(tpl))

