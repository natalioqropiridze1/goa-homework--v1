#scope განსაზღვრავს სად შეუძლია პროგრამას ცვლადის ან ფუნქციის "დანახვა" და გამოყენება


def my_func():
    x = 10  
    print("ფუნქციის შიგნით:", x)

my_func()
 
def outer():
    y = 30  
    def inner():
        print("შიდა ფუნქციაში:", y) 
    inner()

outer()

x = 20  

def show_number():
    print("ფუნქციაში:", x) 

show_number()
print(x)