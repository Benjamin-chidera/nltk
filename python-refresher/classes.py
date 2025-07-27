# define the Vehicle class
class Vehicle:

    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
    
    def car1(self):
        self.color = "red"
        self.value = 60000.00
        self.name = "Fer"
        
        return f"{self.name} is a {self.color} {self.kind} worth ${self.value}"
    
    def car2(self):
        self.color = "blue"
        self.value = 10000.00
        self.name = "Jump"
        
        return f"{self.name} is a {self.color} {self.kind} worth ${self.value}"
        


# test code
# print(car1.description())
# print(car2.description())

car1 = Vehicle()

print("car1: ",car1.car1())


car2 = Vehicle()

print("car2: ",car2.car2())

del car1.color

print(isinstance(car1, Vehicle))
print(isinstance(car2, Vehicle))