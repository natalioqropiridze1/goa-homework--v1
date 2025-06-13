orrect_pin = "1234"  
attempts = 0

while True:
    user_input = input("შეიყვანეთ 4-ციფრიანი PIN კოდი: ")
    attempts += 1

    if user_input == orrect_pin:
        print(" ავტორიზაცია წარმატებით შესრულდა!")
        print(f"ცდების რაოდენობა: {attempts}")
        break
    else:
        print(" არასწორი PIN. სცადეთ ხელახლა.")