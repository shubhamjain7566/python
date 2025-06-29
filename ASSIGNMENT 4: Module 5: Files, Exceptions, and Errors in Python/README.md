# Assignment 4 – Files, Exceptions, and Errors in Python

This repository contains solutions for Assignment 4 from Module 5: **Files, Exceptions, and Error Handling in Python**.

---

## 📂 Task 1: Read a File and Handle Errors
**File:** `task_1.py`

This script:
- Attempts to open and read `sample.txt`
- Prints each line
- Catches `FileNotFoundError` and prints a friendly error message if the file does not exist

### Sample Output (if file exists):
Contents of sample.txt:

This is line 1.
This is line 2.

### Sample Output (if file does not exist):

---

## ✍️ Task 2: Write and Append Data to a File
**File:** `task_2.py`

This script:
1. Writes user input to a file called `output.txt`
2. Appends more data to the same file
3. Reads and displays the entire content of the file after the operations

### Sample Output:
Enter some text to write to the file: Hello
Enter additional text to append to the file: World

Final content of the file:
Hello
World

---

## ▶️ How to Run

Run the scripts using Python 3:

```bash
python task_1.py
python task_2.py