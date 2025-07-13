text = "apple,banana,grape"
fruits = text.split(",") 
print(fruits)  


sentence = "Hello world from Python"
words = sentence.split()  
print(words)  


words = ['hello', 'world']
result = " ".join(words)  
print(result) 

letters = ['a', 'b', 'c']
joined = "-".join(letters) 
print(joined)  


text = "I like apples"
new_text = text.replace("apples", "bananas")  
print(new_text)  

line = "aaa"
fixed = line.replace("a", "b")  
print(fixed) 


text = "   hello   "
clean = text.strip() 
print(clean)  


messy = "___natali__"
cleaned = messy.strip("_")  
print(cleaned)
