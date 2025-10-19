class Account:
    _count = 0 
    def __init__(self, owner, balance):
        self._owner = owner      
        self.__balance = balance  
        Account._count += 1  

    def _show_owner(self):
        print(f"Owner: {self._owner}")

    def __show_balance(self):
        print(f"Balance: {self.__balance}")

    @classmethod
    def get_object_count(cls):
        return cls._count
    
    #Private (__name): (მხოლოდ კლასის შიგნით გამოიყენება)
    #Class method: მეთოდი რომელიც მუშაობს კლასზე და არა კონკრეტულ ობიექტზე