"""https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python"""

def to_jaden_case(string):
    words = string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)