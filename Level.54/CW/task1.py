products = {
    "ხeef": 120,
    "fish": 90,
    "beer": 80,
    "fruit": 150,
    "bread": 70
}

filtered_items = filter(lambda item: item[1] < 100, products.items())
filtered_products = dict(filtered_items)

print(filtered_products)