"https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python"

def is_isogram(string):
    string = string.lower()
    letters = []
    for letter in string:
        if letter in letters:
            return False
        letters.append(letter)
    return True  