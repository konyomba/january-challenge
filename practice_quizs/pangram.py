#a python program to check if a string is a pangram

def check(str):
    #creating a string with all alphabets
    elements = "abcdefghijklmnopqrstuvwxyz"
    #creating a check for char if it entails all aphabets
    for char in elements:
        if char not in str.lower():
            return False
        return True

str = input("Enter string to be checked: ")
#checking is the entered string meets the standard to a pangram or not
if (check(str) == True):
    print("{} : is a pangram".format(str))
else:
    print("{} : is not a pangram".format(str))


