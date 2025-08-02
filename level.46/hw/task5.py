animals = ['tiger', 'lion', 'zebra', 'elephant', 'giraffe']
first_letters = []
for animal in animals:
    first_letters.append(animal[0])
print(first_letters)

first_letters = [animal[0] for animal in animals]
print(first_letters)
