"""https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python"""

#Vowel Count

def count_vowels(s):
 vowels = 'aeiou'
 count = 0
 for char in s.lower():
        if char in vowels:
            count += 1
 return count
