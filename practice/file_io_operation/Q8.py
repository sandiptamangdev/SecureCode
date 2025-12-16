# File Modes Practice
# Open the same file in 'a' mode, add more text, and read it. What is the difference?

with open("hello.txt", "a") as f:
    f.write("\nWelcome to Python.")

with open("hello.txt", "r") as f:
    print(f.read())