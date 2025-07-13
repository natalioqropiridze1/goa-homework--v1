"https://www.codewars.com/kata/55a2d7ebe362935a210000b2/train/python"

def find_smallest_aint(arr):
     smallest = arr[0]
     for num in arr:
        if num < smallest:
            smallest = num
     return smallest
