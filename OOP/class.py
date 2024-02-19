#creating a class in python
class Pen:
    color1 = "Blue"
    
    def __init__(self,id):
        self.id = id
        print("You have created an object")
    
    #creating a method
    def write(self):
        print("I am writting")
        
#creating an object/an instance of a class
first_pen = Pen(id="sl-01")

first_pen.write() #calling the method
#printing attribute
print(f"color of first pen is {first_pen.color1}")
print(f"ID of first pen is {first_pen.id}")

second_pen = Pen(id="sl-02")
print(f"color of second pen is {second_pen.color1}")
print(f"ID of second pen is {first_pen.id}")
    