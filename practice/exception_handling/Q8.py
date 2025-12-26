'''
Dictionary and Attribute Access

Write a function that safely accessess an object's attribute. Handle `AttributeError` if the attribute dosen't exist.

'''
# try:
#     class Dog:
#         def __init__(self, name, age):
#             self.name = name
#             self.age = age
#     my_dog = Dog("sansu", 5)
#     print(my_dog.breed)

# except AttributeError:
#     print("Wrong Attribute")

'''
the code has asked to safely access an object attribute. The above code dosen't satisfy the condition. It works thought!!
'''    

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
def safe_access(obj, attribute):
    try:
        value = getattr(obj, attribute)
        print(f"{attribute}: {value}")
        return value
    except AttributeError:
        print("Wrong Attribute")
        return None

my_dog = Dog("sansu", 5)
safe_access(my_dog, "name")
safe_access(my_dog, "breed")


'''
How do declare function in python?
ans: def function_name():
        pass

How to declare object's attribute or how is object itself first declared?
ans: class Dog:
        def __init__(self, name, age)
                self.name = name
                self.age = age
        my_dog = Dog("sansu", 7)

what is getattr?
ans: it's a built in python function that safely retrives an attribute from an object.
we use getattr so that the program dosen't crash when it fails to find any value.
'''

