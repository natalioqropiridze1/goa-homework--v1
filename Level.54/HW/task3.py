def print_person_info(**kwargs):
    name = kwargs.get('name', 'Unknown')
    age = kwargs.get('age', 0)
    print(f"სახელი: {name}, ასაკი: {age}")