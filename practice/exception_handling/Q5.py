'''
Write a function `read_file(filename)` that:
    - Opens and reads a file
    - Handles `FileNotFoundError` with a message
    - Uses `finally` to ensure the file is always closed
'''

# def read_file(filename):
#     try: 
        # print("Enter a file name: ")
        # filename = input()
        # with open(filename, "r") as f:
        #     print(f.read())
#     except FileNotFoundError:
#         print("Wrong file")
#     finally:
#         print("Program ended")

# read_file("source.txt")

'''
this is good one but the finally has no use as file is opened with `with` so the file should be rather opened manually for the finally to be used.

why use finally?
we should use finally because it runs no matter the file runs or not and when the file is opened it is good one to close the file.
'''

def read_file(filename):
    try:
        file = open(filename, "r")
        print(file.read())
    except FileNotFoundError:
        print("Wrong file")
    finally:
        file.close()

read_file("source.txt")