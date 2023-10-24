import math 

i = 0
all_planks = []

#Getting plank dimensions
class Wood():
    def __init__(self, length,width):
        self.length = length 
        self.width = width

#Calculating area
    def area(self):
        return self.length * self.width

#Checking total number of planks to compare
try:
    total = int(input("How many wooden planks are you comparing: "))
except ValueError:
    print("")

#Getting area
while i < total:
    try:
        l1 = int(input("Length of your wood plank: "))
        try:
            w1 = int(input("Width of your wood plank: "))
            User = Wood(l1,w1)
            all_planks.append(User.area())
        except ValueError:
            print("Invalid")
    except ValueError:
        print("Invalid")
    i += 1

#Comparing areas
final = sorted(all_planks)
print(final)
smallest = final[0]
largest = final[total-1]

#Printing the output
print(f"The smallest plank is {smallest} m² and the largest plank is {largest} m²")
