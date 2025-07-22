numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list = []

for num in numbers:
    if num % 2 != 0: 
        list.append(num * 2)

print(list)

new_list = [num * 2 for num in numbers if num % 2 != 0]
print(list)

numbers = [1, 2, 3, 4, 5]

new_list = ["hello" for num in numbers]
print(new_list)

numbers = [1, 2, 3, 4, 5, 6, 7]

even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)