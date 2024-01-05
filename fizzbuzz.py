number = int(input("Enter a integer number: "))
if (number % 3 == 0) and (number % 5 == 0):
    print("fizzbuzz", number)
elif (number % 3 == 0):
    print("fizz", number)
elif (number % 5 == 0):
    print("buz", number)
else:
    print(number)
