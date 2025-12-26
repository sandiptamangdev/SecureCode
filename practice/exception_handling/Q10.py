'''
Write a program with nested `try/expect` blocks that:
    - Reads a file
    - Converts lines to integers
    - Calculates the sum
    - Handles `FileNotFoundError`,
    - `ValueError`, and `ZeroDivisionError`
'''

try: 
    with open("number.txt", "r") as f:
        content = f.read()
        
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Value Error")
except ZeroDivisionError:
    print("Cannot be divided by Zero")
