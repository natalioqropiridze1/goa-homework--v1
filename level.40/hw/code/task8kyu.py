"https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python"

def find_short(s):
    words = s.split()         
    lengths = []             
    for word in words:
        lengths.append(len(word))
    lengths.sort()
    return lengths[0]