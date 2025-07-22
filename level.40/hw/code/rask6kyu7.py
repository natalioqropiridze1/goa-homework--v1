"https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python"

def solution(text, ending):
    lenght_text = len(text)
    len_ending = len(ending)

    return text[len_ending:] == ending
    