def check_age(age):
    if age < 0:
        raise ValueError("ასაკი არ შეიძლება იყოს უარყოფითი")
    return f"ასაკი სწორია: {age}"