# 📘 Day 3 – Conditionals

**Main Topics:**

- Using `if`, `elif`, and `else` to control logic flow
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Boolean expressions
- Indentation and block structure

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Use `if`, `elif`, and `else` statements
- Write conditional logic to control program behavior
- Apply comparison and logical operators
- Create programs that make decisions based on input

---

## 🔀 Conditionals Overview

Conditionals let your program make decisions based on conditions.

### ✅ Syntax:

```python
if condition:
    # block of code if condition is true
elif another_condition:
    # block if the above is false but this is true
else:
    # block if all conditions are false
```

---

### 📝 Example:

```python
age = int(input("Enter your age: "))

if age < 13:
    print("You're a child.")
elif age < 18:
    print("You're a teenager.")
else:
    print("You're an adult.")
```

---

## 📝 Assignment 1: Grade Classifier

Write a program that:

- Takes a numeric score input from the user (0–100)
- Prints a letter grade based on the score:

| Score Range | Grade |
| ----------- | ----- |
| 90–100      | A     |
| 80–89       | B     |
| 70–79       | C     |
| 60–69       | D     |
| Below 60    | F     |

### ✅ Example:

```python
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

---

## 📝 Assignment 2: Odd or Even Checker

Write a program that:

- Asks the user to enter a number
- Prints whether it is odd or even

### ✅ Example:

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
```

---

## 💡 Tips:

- Remember to indent properly (4 spaces or 1 tab)
- Use `elif` to avoid multiple nested `if`s
- Test with different input values to check all branches

---

Contact me anytime when you have the problem: anatwork14@gmail.com
