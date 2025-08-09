#字母顺序正排序，倒排序
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

#对列表进行临时排序
cars = ['bmw','audi','toyota','subaru']

print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#对列表元素进行倒叙
cars = ['bmw','audi','toyota','subaru']
cars.reverse()
print("\nHere is the reverse list:")
print(cars)