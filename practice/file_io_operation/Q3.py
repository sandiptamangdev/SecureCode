# Basic File Operations.
# Append `"Welcome to Python"` to the same file.

with open("example.txt", "a") as f:
    f.write("\nWelcome to python")
    
with open("example.txt", "r") as f:
    print(f.read())