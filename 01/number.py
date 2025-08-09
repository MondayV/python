#打印1-6的数字，不包括6
numbers= list(range(1,6))
print(numbers)

#打印1~10内的偶数：
even_numbers = list(range(2,11,2))
print(even_numbers)

#输出一个数列，大小为每个顺序的平方数
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)