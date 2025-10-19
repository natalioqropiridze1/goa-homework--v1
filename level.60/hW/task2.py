class Library:
    def __init__(self, books, secret_code):
        self._books = books
        self.__secretCode = secret_code

    @staticmethod
    def calculate_late_fee(days_late, fee_per_day):
        return days_late * fee_per_day