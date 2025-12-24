'''
Basic Exception Handline

Write a program that converts a string to an integer. Handle the case where conversion fails with `ValueError`.
'''
try:
    print("Enter a value: ")
    value1 = int(input())
    print(type(value1))
except ValueError:
    print('Wrong value')




'''
typeof is from javasciprt where as in python it is type() typeof in js can be used without the paranthesis typeof value1 vs python type(value1)
'''