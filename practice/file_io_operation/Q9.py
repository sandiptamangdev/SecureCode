# Advance / Scenario
# Write a program to count how many lines and words are in a file.

# with open("hello.txt", "r") as f:
#     for i, line in enumerate(f, start=1):
#         pass # What is pass?
#     print(f"Number of lines in the file: {i}")

with open("hello.txt", "r") as f:
    lines = f.readlines()


with open("hello.txt", "r") as f:
    content = f.read()
    word_count = len(content.split())
print(f"Number of words: {word_count}")
