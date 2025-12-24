'''
Basic Exception Handling

Write a program that accesses a list element by index. Handle `IndexError` if the index is out of range.
'''

try:
    mylist = [1, 2, 3, 4, 5]
    # print(mylist)
    print("Enter a index to access a list item: ")
    index = int(input())
    print(f"Value at index {index} is {mylist[index]}")
except IndexError:
    print("Wrong index")