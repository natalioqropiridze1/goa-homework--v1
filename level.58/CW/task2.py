class Fighter:
    def __init__(self, name, power, health):
        self.name = name    
        self.power = power   
        self.health = health  

    def info(self):
        print(f"სახელი: {self.name}, ძალა: {self.power}, სიცოცხლე: {self.health}")

fighter1 = Fighter("Bruce Lee", 95, 100)
fighter2 = Fighter("Jackie Chan", 85, 110)
fighter3 = Fighter("Chuck Norris", 99, 120)


print(fighter2.name)  
print(fighter2.power)  
print(fighter2.health) 

fighter3.info()
