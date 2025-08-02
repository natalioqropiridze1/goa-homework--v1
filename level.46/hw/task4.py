mixed = [2, 5, 8, 11, 14, 17, 20]

evens = [num for num in mixed if num % 2 == 0]
print(evens)

odds = [ num for num in mixed if num %2 == 1]
print(odds)