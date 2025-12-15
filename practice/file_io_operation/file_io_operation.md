## **1. Key Theory**

### **1.1 `open()` Function**

* **Purpose:** Open a file and return a file object to perform operations.
* **Syntax:** `open(filename, mode)`
* **Common Modes:**

  | Mode   | Description                                           |
  | ------ | ----------------------------------------------------- |
  | `'r'`  | Read (default). File must exist.                      |
  | `'w'`  | Write. Creates a new file or truncates existing file. |
  | `'a'`  | Append. Adds data to the end of the file.             |
  | `'rb'` | Read in binary mode.                                  |
  | `'wb'` | Write in binary mode.                                 |

---

### **1.2 Reading Files**

* `read()` → Reads entire file content as a string.
* `read(size)` → Reads up to `size` characters/bytes.
* `readline()` → Reads one line at a time.
* `readlines()` → Reads all lines as a list.

---

### **1.3 Writing Files**

* `write(string)` → Writes string to file (overwrites in `'w'`, appends in `'a'`).
* `writelines(list_of_strings)` → Writes multiple strings at once.
* Important: Always check file mode; `'r'` cannot write, `'w'` overwrites, `'a'` appends.

---

### **1.4 Closing Files**

* Always close a file to free resources: `file.close()`.
* **Better practice:** Use `with` statement for automatic closing:

```python
with open("file.txt", "r") as f:
    data = f.read()
```

---

## **2. Practical Questions / Exercises**

### **Basic File Operations**

1. Create a file named `example.txt` and write `"Hello World"` to it.
2. Open `example.txt` and read its content. Print it.
3. Append `"Welcome to Python"` to the same file.

---

### **Line-Based Operations**

4. Create a file `numbers.txt` and write numbers 1 to 5, each on a new line.
5. Read `numbers.txt` line by line and print each line with its line number.
6. Read all lines into a list and print the list.

---

### **File Modes Practice**

7. Open a file in `'w'` mode, write some text, then read it. What happens?
8. Open the same file in `'a'` mode, add more text, and read it. What is the difference?

---

### **Advanced / Scenario**

9. Write a program to count how many lines and words are in a file.
10. Write a program that copies content from `source.txt` to `destination.txt`.
11. Write a program to reverse the lines in a file (last line becomes first, etc.).

---


