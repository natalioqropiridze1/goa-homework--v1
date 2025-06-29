
fruits = ["apple", "banana", "apple", "cherry"]
colors = ["red", "blue", "green","green.", "blue"]
numbers = [5, 2, 9, 1, 5]

# აბრუნებს ელემენტის ინდექსს
print(fruits.index("banana"))  

# რამდენჯერ გვხვდება ელემენტი
print(fruits.count("apple"))  

#  ალაგებს ზრდის მიხედვით 
numbers.sort()
print(numbers)  

# აბრუნებს ახალ სიას სადაც ერთნაირი ელემეტები ერთად არის დალაგებული
print(sorted(colors))  

#აბრუნებს მინიმალურ მნიშვნელობას
print(min(numbers))  

#აბრუნებს მაქსიმალურ მნიშვნელობას
print(max(numbers))
