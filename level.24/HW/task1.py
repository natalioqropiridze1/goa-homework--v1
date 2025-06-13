word = input("შეიყვანეთ სიტყვა: ")


reversed_word = word[::-1]

if word == reversed_word:
    print("ეს სიტყვა განსაკუთრებულია (Palindrome)!")
else:
    print("ეს ჩვეულებრივი სიტყვაა.")
