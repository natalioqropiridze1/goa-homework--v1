numbers = {1, 3, 5, 7, 9}
print(" set1:", numbers)
numbers.add(11)     
numbers.add(13) 

numbers.remove(3)  
numbers.remove(7)   

other_numbers = {3, 5, 8, 11}
print("set2:", other_numbers)
union_set = numbers.union(other_numbers)
print( union_set)

intersection_set = numbers.intersection(other_numbers)
print(intersection_set)

difference_set = numbers.difference(other_numbers)
print( difference_set)
