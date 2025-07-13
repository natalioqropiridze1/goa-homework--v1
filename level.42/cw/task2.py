# Dictionary არის მონაცემთა ტიპი რომელიც ინახავს key : value ელემენტებს
# გამოიყენება ინფორმაციის  შესანახად  მაგალითად, ადამიანის მონაცემების
person = {
    "name": "Ana",
    "hobby": "reading",
    "height": 165,
    "weight": 55
}
print("ლექსიკონი", person)

print("სახელი:", person.get("name"))   
print("ასაკი:", person.get("age"))    

person.update({"weight": 56})          
person.update({"age": 25})             

print("გასაღებები:", person.keys())
print("მნიშვნელობები:", person.values())
print("წყვილები:", person.items())


removed_hobby = person.pop("hobby")
print("წაშლილი ჰობი:", removed_hobby)


person.clear()
