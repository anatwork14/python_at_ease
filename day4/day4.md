# 📘 Day 4 – Loops

**Main Topics:**

- `for` loops for iterating over ranges and sequences
- `while` loops for conditional repetition
- Loop control: `break`, `continue`, `pass`
- Practical examples of repeated tasks

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Use `for` and `while` loops to repeat code
- Write loops that iterate over numbers, lists, and strings
- Use nested loops for patterns or tables
- Apply loop control statements effectively

---

## 🔁 Loop Overview

### ✅ `for` loop

Used to repeat an action a fixed number of times (usually over a range or iterable).

```python
for i in range(5):
    print(i)
```

### ✅ `while` loop

Used when the number of repetitions is unknown but based on a condition.

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

---

## 📝 Assignment 1: Sum from 1 to n

Write a program that:

- Asks the user for a number `n`
- Computes the sum `1 + 2 + ... + n` using a loop

### ✅ Example:

```python
n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum from 1 to", n, "is", total)
```

---

## 📝 Assignment 2: Multiplication Table

Write a program that:

- Asks the user to input a number
- Prints the multiplication table for that number (from 1 to 10)

### ✅ Example:

```python
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

---

## 📝 Assignment 3: Star Triangle Pattern

Write a program that:

- Asks the user to input a height `n`
- Prints a left-aligned triangle of stars

### ✅ Example (n = 4):

```
*
**
***
****
```

```python
n = int(input("Enter triangle height: "))

for i in range(1, n + 1):
    print("*" * i)
```

---

## 💡 Tips:

- Use `range(start, end)` in `for` loops
- `break` exits a loop early, `continue` skips to the next iteration
- Use nested loops for grids or pattern generation

---

Contact me anytime when you have the problem: anatwork14@gmail.com
