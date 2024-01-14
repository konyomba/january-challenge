#a python program that checks if a given string is a palindrom

def palindrom(str):
    return str[::-1]

str = input("Enter string to be checked: ")
if str == str[::-1]:
    print("{} : string is palindrom".format(palindrom(str)))
else:
    print("{} :not a palindrom".format(palindrom(str)))
