def print_start_end(func):
    def wrapper(*args, **kwargs):
        print("ფუნქცია დაიწყო")
        result = func(*args, **kwargs)
        print("ფუნქცია დასრულდა")
        return result
    return wrapper