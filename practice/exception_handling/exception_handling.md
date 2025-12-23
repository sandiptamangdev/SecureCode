## **1. Key Theory**

### **1.1 Exception Handling Basics**

* **Purpose:** Catch and handle errors gracefully instead of crashing the program.
* **Exception:** An event that occurs during program execution that disrupts the normal flow.
* **Key Components:**
  - `try` → Code block where an exception might occur
  - `except` → Catches and handles specific exceptions
  - `finally` → Always executes, used for cleanup (optional)
  - `else` → Executes if no exception occurred (optional)

---

### **1.2 `try/except` Block Structure**

**Basic Syntax:**

```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle this specific exception
    print("Cannot divide by zero!")
```

**With Multiple Exceptions:**

```python
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Invalid input! Enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
```

---

### **1.3 Common Exception Types**

| Exception | Cause |
| --- | --- |
| `ZeroDivisionError` | Division by zero: `10 / 0` |
| `ValueError` | Invalid value: `int("abc")` |
| `TypeError` | Wrong type: `"5" + 5` |
| `IndexError` | Invalid list index: `list[100]` |
| `KeyError` | Missing dictionary key: `dict["missing"]` |
| `FileNotFoundError` | File doesn't exist: `open("missing.txt")` |
| `AttributeError` | Invalid attribute: `obj.missing_attr` |
| `NameError` | Undefined variable: `print(undefined_var)` |

---

### **1.4 The `finally` Block**

* **Purpose:** Executes regardless of whether an exception occurred (cleanup code).
* **Use Cases:** Close files, release resources, end database connections.

```python
try:
    file = open("data.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    file.close()  # Always executes
```

---

### **1.5 Exception Order Matters**

* Catch **specific exceptions first**, then general ones.
* `Exception` catches most built-in exceptions.
* `BaseException` catches nearly everything (use rarely).

```python
try:
    value = int(input())
except ValueError:          # Specific - catches first
    print("Not a number!")
except Exception:           # General - catches second
    print("Some other error!")
except BaseException:       # Most general - catches last
    print("Unexpected error!")
```

---

### **1.6 `else` and Full Structure**

```python
try:
    value = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print(f"You entered: {value}")  # Runs if NO exception
finally:
    print("Processing complete!")  # Always runs
```

---

## **2. Practical Questions / Exercises**

### **Basic Exception Handling**

1. Write a program that asks the user for two numbers and divides the first by the second. Handle `ZeroDivisionError` and `ValueError`.

2. Write a program that converts a string to an integer. Handle the case where conversion fails with `ValueError`.

3. Write a program that accesses a list element by index. Handle `IndexError` if the index is out of range.

---

### **File Operations with Exception Handling**

4. Write a program that opens a file, reads its content, and prints it. Handle `FileNotFoundError` gracefully.

5. Write a function `read_file(filename)` that:
   - Opens and reads a file
   - Handles `FileNotFoundError` with a message
   - Uses `finally` to ensure the file is always closed

6. Write a program that reads a CSV file and converts each value to an integer. Handle both `FileNotFoundError` and `ValueError`.

---

### **Dictionary and Attribute Access**

7. Write a program that accesses a dictionary key. Handle `KeyError` if the key doesn't exist.

8. Write a function that safely accesses an object's attribute. Handle `AttributeError` if the attribute doesn't exist.

9. Write a program that processes a list of dictionaries, extracting a field from each. Handle cases where the field is missing.

---

### **Advanced / Scenario-Based**

10. Write a program with nested `try/except` blocks that:
    - Reads a file
    - Converts lines to integers
    - Calculates the sum
    - Handles `FileNotFoundError`, `ValueError`, and `ZeroDivisionError`

11. Write a function `safe_divide(a, b)` that:
    - Attempts division
    - Handles `ZeroDivisionError` and `TypeError`
    - Uses `else` to print the result only if successful
    - Uses `finally` to log that the operation completed

12. Write a program that retries reading user input up to 3 times if they enter invalid data. If all 3 attempts fail, raise a custom message.

---

## **3. Challenge Problem**

**Question 13:** Write a robust data processor that:
- Opens a file containing numbers (one per line)
- Converts each line to an integer
- Calculates the average of valid numbers
- Handles `FileNotFoundError` with a clear message
- Handles `ValueError` for invalid lines (log error, continue processing)
- Uses `finally` to ensure the file is closed
- Returns the average or `None` if no valid data exists
- Prints a summary: total lines, valid numbers, skipped lines

**What exceptions must you catch? In what order? Why does order matter?**