#a program that takes a temperature in celcius and converts it to kelvins

temp = float(input("Enter temperatures in degrees celcius.[eg 12.2]: "))
def kelvin(a):
    return (a+273.15)
print("The tem in kelvin is: ",kelvin(temp))
