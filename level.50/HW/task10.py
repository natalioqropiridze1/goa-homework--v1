nums = [1, 2, 3, 4, 5, 6]
even_plus_10 = list(map(lambda x: x + 10, filter(lambda x: x % 2 == 0, nums)))
print(even_plus_10)