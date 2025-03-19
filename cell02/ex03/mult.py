#!/bin/python3
number1 = int(input("Enter the number"))
number2 = int(input("Enter the number"))
result = number1*number2
print(f"{number1} x {number2} = {result}")
if result > 0:
    print("This number is positive")
elif result < 0:
    print("This number is negative")
else:
    print("This number is zero")