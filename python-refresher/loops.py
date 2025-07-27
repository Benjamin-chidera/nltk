from random import choice
# for i in range(10):
#     print(i)
    
    
    
myList = ["apple", "banana", "cherry"]

for x in choice(myList):
    print(x)
    
    
del myList[1]

print(myList)


my_Set = set(["apple", "banana", "cherry", "apple"])

print(my_Set)


a, b = (0 ,1)

print(a, b)


f_1: float = 1.1
f_2 = float(2.0)

print(f_1, f_2)

str: str = "apple"

print(type(str))