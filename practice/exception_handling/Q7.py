'''
Dictionary and Attribute Access

Write a program that accesses a dictionary key. Handle `KeyError` if the key dosen't exist.
'''

'''
How is dictionary declared in python?

Ans: my_dict = {"name": Kimmy, "age": 30, "city": "new land mars" }

what is dictionary key?

Ans: From the above dictionary name is the key and the kimmy is the value.

'''
try:
    my_dict = {"name": "sansu", "age": 7, "breed": "doberman"}

    print("Enter a key: ")
    key = my_dict[input()]
    # value = my_dict[key]
except KeyError:
    print("Wrong key")
else:
    print(key)





