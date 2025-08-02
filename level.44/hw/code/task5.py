"""https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python"""

def digitize(n):
    digits = []
    if n == 0:
        return [0]
    while n > 0:
        digits.append(n % 10)  
        n = n // 10         
    return digits