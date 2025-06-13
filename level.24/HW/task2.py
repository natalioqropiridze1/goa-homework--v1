words = ["apple", "banana", "cherry", "date", "fig", "grape"]

rev = words[::-1]  

i = 0
for words in rev:
    if i % 2 == 0:
        print(words)
    i += 1