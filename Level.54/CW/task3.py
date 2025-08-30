def my_decorator(func):
    def wrapper():
        print("Before greeting")
        func()
        print("After greeting")
    return wrapper

@my_decorator
def greet():
    print("Hello World")


greet()