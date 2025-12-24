'''
Write a program that reads a CSV file and converts each value to an integer. Handle both `FileNotFoundError` and `ValueError`.
'''

# with open("yo.csv", "w") as f:
#     pass

# with open("num.csv", "w") as f:
#     f.write("1")
# try:
#     print("Enter the file name: ")
#     filename = input()
#     with open(filename, "r") as f:
#         content = f.read()
#         convert = int(content)
# except FileNotFoundError:
#     print("Wrong file")
# except ValueError:
#     print("Wrong value")
# else: 
#     print(convert)

try:
    print("Enter the file name: ")
    filename = input()

    with open(filename, "r") as f:
        content = f.read()

    values = content.split(",")
    print(values)
    converted_values = []

    # have to review this part
    for value in values:
        cleaned_value = value.strip()
        converted_values.append(int(cleaned_value))
    
    print("Converted values:", converted_values)

except FileNotFoundError:
    print("Wrong file")
except ValueError:
    print("Wrong value")
else:
    print("Converted Sucessfully")
'''
What is CSV file?

CSV = comma seperated value

format: plain text
data type: text only
formating: none(no colors, fonts, or bold)
capacity: no inherent(depends on software)

its Universal Compatibility makes it really good to use like most editor and software can open this.

When to use csv:

Data exchange
Data backup
Reporting

example how it stores data:

ID,ProductName,Price,InStock
101,Wireless Mouse,25.99,Yes
102,Mechanical Keyboard,89.00,No
103,USB-C Cable,12.50,Yes
'''

