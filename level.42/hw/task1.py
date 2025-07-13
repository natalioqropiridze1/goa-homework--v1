numbers = set()  
numbers.add(5)   
numbers.add(10)

numbers.remove(5) 
numbers.remove(10)

even_numbers = {2, 4, 6, 8}

union_set = numbers.union(even_numbers)
intersection_set = numbers.intersection(even_numbers)
difference_set = numbers.difference(even_numbers)

print("union:", union_set)
print("intersection:", intersection_set)
print("difference:", difference_set)