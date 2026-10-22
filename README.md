# Python Practice

A collection of **139 Python programs** covering the core fundamentals of the language: conditional statements, loops, and string handling.

Every program is saved in its own `.py` file with the question at the top, the solution in the middle, and the **actual output from a real run** at the bottom.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Programs](https://img.shields.io/badge/Programs-139-green)

---

## Repository Structure

```
python-practice/
├── 01_Conditional_Statements/   (50 programs)
├── 02_For_While_Loops/          (49 programs)
└── 03_String_Methods/           (40 programs)
```

| Folder | Topic | Programs |
|---|---|---|
| `01_Conditional_Statements` | `if`, `elif`, `else`, nested `if`, `match case` (no loops) | 50 |
| `02_For_While_Loops` | `for` loop, `while` loop, patterns, number and string logic | 49 |
| `03_String_Methods` | Built-in string methods and string manipulation | 40 |
| | **Total** | **139** |

---

## Topics Covered

**01 - Conditional Statements**
- Basic decisions: positive/negative, even/odd, voting eligibility, leap year
- Comparing numbers, finding the greatest and smallest of three numbers
- Grades, exam results, ticket pricing, bonus, electricity bill, discounts
- Nested `if`: password validation, loan and exam eligibility
- `match case`: weekday names, calculator, traffic signal, ATM menu

**02 - For and While Loops**
- Number series, tables, squares, cubes, factorial, Fibonacci
- Digit operations: reverse, palindrome, sum, largest and smallest digit
- Prime, Armstrong and strong numbers
- Star and number patterns
- String loops: vowels, consonants, ASCII values, reverse, palindrome
- User-input loops and a menu-driven program

**03 - String Methods**
- Case conversion: `upper()`, `lower()`, `capitalize()`, `title()`, `swapcase()`
- Searching and checking: `find()`, `count()`, `startswith()`, `endswith()`, `isalpha()`, `isdigit()`, `isalnum()`, `isidentifier()`
- Editing: `strip()`, `replace()`, `split()`, `join()`
- Extraction and cleanup: digits, alphabets, punctuation, duplicate characters
- Word-level tasks: longest word, shortest word, word count

---

## File Format

Each file follows the same layout:

```python
# Question 23: Write a program to calculate electricity bill based on units consumed.

units = int(input("Enter units consumed: "))

# First 100 units : Rs.5 per unit
# Next 100 units  : Rs.7 per unit
# Above 200 units : Rs.10 per unit
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10

print("Total electricity bill: Rs.", bill)


# ----- Output -----
# Enter units consumed: 250
# Total electricity bill: Rs. 1700
```

The output is stored as comments, so every file stays a valid, runnable Python script.

---

## How to Run

1. Make sure **Python 3.10 or higher** is installed (the `match case` programs need it).

   ```bash
   python --version
   ```

2. Clone the repository:

   ```bash
   git clone https://github.com/satyamkurhe/python-practice.git
   cd python-practice
   ```

3. Run any program:

   ```bash
   python 01_Conditional_Statements/q05_leap_year.py
   ```

---

## What I Learned

- Writing clear decision-making logic with `if`, `elif`, `else` and `match case`
- Using `for` and `while` loops to solve number, pattern and string problems
- Using Python's built-in string methods effectively
- Taking user input and handling it correctly
- Breaking a problem into small steps and writing clean, readable code

---

## Author

**Satyam Kurhe**
GitHub: [@satyamkurhe](https://github.com/satyamkurhe)

---

If you find this repository helpful, consider giving it a star.
