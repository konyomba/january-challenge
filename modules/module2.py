#test for functions created and stored in module1.py 
#function mul from module1 is the only function that cannot be imported

from module1 import add

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

print("{} + {} = {}".format(num1, num2, add(num1,num2)))
