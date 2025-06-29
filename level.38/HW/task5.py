def count_unique(list):
    for item in list:
        print(item, "-", list.count(item))
        
count_unique(["apple", "banana", "apple"])
