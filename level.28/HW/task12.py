text = "I visited Georgia, Armenia and Greece"
search_word = input("შეიყვანეთ საძიებელი სიტყვა: ")

position = text.find(search_word)

if position != -1:
    print(f"სიტყვის პოზიციაა: {position}")
else:
    print("word not found")
