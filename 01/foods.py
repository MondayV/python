my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]  #提取一个副本切片，复印到新的列表

#friend_foods = my_foods  这样会导致两个变量指向同一个列表，即使进行不同的元素添加也会出现在同一列表中

my_foods.append("cannoli")   #添加不同元素
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend a favorite foods are:")
print(friend_foods)