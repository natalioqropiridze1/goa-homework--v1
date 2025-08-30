def check_word(word):
    if word == "":
        raise ValueError("სიტყვა არ უნდა იყოს ცარიელი")
    return f"სიტყვა სწორია: {word}"