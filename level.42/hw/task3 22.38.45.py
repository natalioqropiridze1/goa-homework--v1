student = {
    'name': 'Nino',
    'hobby': 'Reading',
    'height': 170,
    'weight': 65
}
name = student.get('name')  
height = student.pop('height')  

print("Name:", name)
print("Removed height:", height)
print("Student after pop:", student)
