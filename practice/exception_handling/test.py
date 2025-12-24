'''
Exception Handeling is basically handelling errors rather than crashing the program.
There are key components of exception handeling are try, except, finally, else.
'''


# print("Enter a number: ")
# num1 = int(input())
# print("Enter another number: ")
# num2 = int(input())

# try:
#     result = num1 / num2
#     print(result)
# except ZeroDivisionError:
#     print("Cannot divide by zero")

while True:
    try:
        print("Enter a number: ")
        num1 = int(input())
        print("Enter another number: ")
        num2 = int(input())
        result = num1 / num2
        # print(result)
        # break 

        ''' exiting the loop when the program runs sucessfully there is also continue that skips to the next iteration.'''

    except ZeroDivisionError:
        print("Cannot divide by zero")
        # raise


    # except OverflowError:
    #     print("Number too large")
    # except FloatingPointError:
    #     print("floating point calculation issue")
    # except TypeError:
    #     print("Wrong date type")

    except ValueError:
        print("Wrong value")
        # raise
    else:
        print(f"Result: {result}") 
        '''
        raise will catch the valueerror and throw the error ending the program and showing where the error happened.
        '''
'''
typeError is basically useless in this and overflowerror and floatingpointerror not even going to be seen in this kind of small program and only the valueError and zerodivisiableerros seems the only one that is going to be used most or only can be used
'''


'''
Python has quite a few built-in exceptions. Here are some of the most common ones:

**Arithmetic/Numeric Errors:**
- `ZeroDivisionError` — dividing by zero
- `OverflowError` — number too large
- `FloatingPointError` — floating point calculation issue

**Type/Value Errors:**
- `TypeError` — wrong data type (e.g., adding a string to an integer)
- `ValueError` — wrong value (e.g., `int("abc")`)
- `IndexError` — accessing an index that doesn't exist in a list
- `KeyError` — accessing a key that doesn't exist in a dictionary

**Name/Attribute Errors:**
- `NameError` — variable doesn't exist
- `AttributeError` — object doesn't have that attribute

**File/IO Errors:**
- `FileNotFoundError` — file doesn't exist
- `IOError` — general input/output error
- `PermissionError` — no permission to access file

**Other Common Ones:**
- `ImportError` — can't import a module
- `RuntimeError` — general runtime problem
- `NotImplementedError` — method not implemented yet
- `StopIteration` — iteration is done

You can see a complete list in the Python documentation, but these cover most everyday scenarios. The cool thing is you can also create your own custom exceptions by inheriting from the `Exception` class!
'''
