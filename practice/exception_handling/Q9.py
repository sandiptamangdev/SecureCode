'''
Dictionary and Attribute Access

Write a program that processes a list of dictionaries, extracting a field from each. Handle cases where the field is missing.
'''
my_dict = {"name": "timmy", "age": 2, "breed": "mouse"}

print(my_dict["name"])
print(my_dict["age"])
print(my_dict["breed"])

print("\nWhat if the key dosen't exist")

# print(my_dict[color])
# instead of this we can make use of get() to safely get a value.
print(my_dict.get("color"))
print(my_dict.get("color", "Not Found"))

print("\nProcessing a list of dictioneries")

animals = [
    {"name": "timmy", "age": 2, "breed": "mouse"},
    {"name": "fluffy", "age": 6},
    {"name": "ginger", "breed": "cat"}
]

# for animal in animals:
#     name = animal.get("name", "Unknown")
#     print(f"Name:", name)

# print("\nNow we need to add those into a list")

# names = []
# for animal in animals:
#     name = animal.get("name", "Unknown")
#     names.append(name)

# print(names)

for animal in animals:
    age = animal.get("age", "Unknown")
    print(f"Age:", age)

print("\nNow we need to add those into a list")

ages = []
for animal in animals:
    age = animal.get("age", "Unknown")
    ages.append(age)

print(ages)
'''
What do you mean by field in the Dictionary?
ans: Key-value pair field.

What do you mean by field is missing if key-value pair is field then is it missing of one of the key or value?
ans: It means the asked field itself dosen't exist.
'''




