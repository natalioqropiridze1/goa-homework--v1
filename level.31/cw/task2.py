def square_info(length=10):
    area = length * length
    perimeter = 4 * length
    return area, perimeter

square_area1, square_perimeter1 = square_info(6)
square_area2, square_perimeter2 = square_info()

print("სიგრძე 6:")
print("ფართობი:", square_area1)
print("პერიმეტრი:", square_perimeter1)