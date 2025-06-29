
my_list = [1, 2, 3, 4, 2]
# შეცვლა შესაძლებელია
my_list[0] = 10
print(my_list)  
# დუბლიკატებიც არის ნებადართული
print(my_list.count(2))  



my_tuple = (5, 6, 7, 5)
# უცვლელია – შეცვლა არ შეგვიძლია
# my_tuple[0] = 100  
# დუბლიკატები დასაშვებია
print(my_tuple.count(5)) 


my_set = {1, 2, 3, 3, 4}
# ავტომატურად შლის დუბლიკატებს
print(my_set)  
# შეგვიძლია ელემენტების დამატება
my_set.add(5)
print(my_set)  
# შეგვიძლია ელემენტების წაშლა
my_set.remove(2)
print(my_set) 
