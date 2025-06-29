def manual_index(list, element):
    i = 0
    for item in list:
        if item == element:
            return i
        i += 1
    return -1

