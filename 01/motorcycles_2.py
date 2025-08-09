motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
#弹出一个值
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#弹出指定的值
motorcycles = ['honda','yamaha','suzuki']

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

#指定元素索引删除
motorcycles = ['honda','yamaha','suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# 根据值删除元素
motorcycles = ['honda','yamaha','suzuki',"ducati"] 
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")