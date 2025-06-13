def new_greet(first_name, last_name):
    print(f"Greetings {first_name} {last_name}")

new_greet("John", "Doe")
new_greet("Nino", "Beridze")

# ფუნქციის პარამეტრები: first_name და last_name
# პარამეტრები არის ცვლადები, რომლებიც ფუნქციის აღწერისას ვიყენებთ.
# ისინი ფუნქციას აძლევენ შესაძლებლობას მიიღოს მონაცემები.

def new_greet(first_name, last_name):
    # აქ ვიყენებთ პარამეტრებს ფუნქციის შიგნით
    print(f"Greetings {first_name} {last_name}")

# არგუმენტები: "John" და "Doe"
# არგუმენტები არის რეალური მნიშვნელობები რომლებიც ფუნქციის გამოძახებისას პარამეტრებს გადაეცემათ.
new_greet("John", "Doe")  # არგუმენტები გადაეცემა პარამეტრებს
