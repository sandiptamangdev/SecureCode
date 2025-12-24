'''
File Operation with Exception Handling

Write a program that opens a file, reads its content, and prints it. Handle `FileNotFoundError` gracefully.
'''

# try:
#     print("Enter the file name: ")
#     filename = input()
#     # with open(f"{filename}", 'r') as f:
#     with open(filename, "r") as f:
#         # content = f.read()
#         # pass
#         print(f.read())
# except FileNotFoundError:
#     print("File not found")
# except PermissionError:
#     print("You don't have permission to read this file")
# else:
#     print(f.read())
# else:
#     print(content)

'''
why even use else
else is best practice for handleling the error.

you can't use print(f.read()) as else beacuse pass does nothing to the opened file and it closes and when it comes down to the else to read it the file is already close.

while with content as a variable it's good to have used else but then again it's use of extra var where memeory is used so best to save memory when we can.

we can make use of here just filename then f"{filename}" because it's just one of the value and with no other strings.

why not try manually to make use of the best practices which is more flexible the with.

'''

try:
    print("Enter the file name:")
    filename = input()
    file = open(filename, "r")
except FileNotFoundError:
    print("Wrong File")
else:
    print(file.read())
    file.close()