def manual_max(my_list):
    max_value = my_list[0]
    for item in my_list:
        if item > max_value:
            max_value = item
    return max_value



def manual_len(sequence):
    count = 0
    for _ in sequence:
        count += 1
    return count

