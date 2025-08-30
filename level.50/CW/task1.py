nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = list(map(lambda x: x ** 2, nums))
print("squares:", squares) 
even = list(filter(lambda x: x % 2 == 0, nums))
print("even:", even)


