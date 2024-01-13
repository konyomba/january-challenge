#a function that reverses a string
element = input("Enter a string to be reversed: ")
def rev_str(input_str):
    return input_str[::-1]

print("reversed str: ",rev_str(element))
