def greet_people(special, *guests, **visitors):
    print(f"hello {special}! you are special guest ")
    
    for guest in guests:
        print(f"hello {guest}! happpy u're here")

    for visitors in visitors.items():
        print(f"hello  {visitors} ")
