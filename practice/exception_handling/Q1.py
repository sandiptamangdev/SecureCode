'''
Basic Exception Handling

Write a program that asks the user for two numbers and divides the first by the second. Handle `ZeroDivisionError` and `ValueError`.
'''
try:
    print("Enter a number: ")
    num1 = int(input())

    print("Enter another number: ")
    num2 = int(input())

    result = num1 / num2
except ZeroDivisionError:
    print("Cannot be divided by 0.")
except ValueError:
    print("Wrong value.")
else: 
    print("Result:", result)

