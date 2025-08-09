motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

#列表修改元素
motorcycles[0] = 'ducati'
print(motorcycles)

#列表末尾添加元素
motorcycles.append('ducati')
print(motorcycles)

#列表插入元素
motorcycles.insert(0,'ducati')
print(motorcycles)

#列表删除元素
del motorcycles[0]
print(motorcycles)

del motorcycles[3]
print(motorcycles)