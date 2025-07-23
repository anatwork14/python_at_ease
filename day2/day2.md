# 📘 Day 2 – Variables & Data Types

**Main Topics:**

- Variable declaration and naming rules
- Built-in data types: `int`, `float`, `str`, `bool`
- Basic operations and expressions
- Type conversion with `int()`, `float()`, `str()`, `bool()`

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Declare and use variables in Python
- Perform arithmetic operations using different data types
- Convert between types
- Understand how boolean logic works

---

## 🧠 Variable Declaration and Naming Rules

- Variables are used to **store data** in Python.
- You **don't need to declare a type** — Python is dynamically typed.

### ✅ Rules for naming variables:

- Must start with a letter or underscore (`_`)
- Cannot start with a number
- Can contain letters, digits, and underscores
- Case-sensitive (`age` ≠ `Age`)
- Avoid using Python keywords like `for`, `if`, `class`

### 📝 Examples:

```python
age = 21
user_name = "An"
_total = 1000
```

## 🔢 Built-in Data Types

| Type    | Description          | Example           |
| ------- | -------------------- | ----------------- |
| `int`   | Integer numbers      | `x = 10`          |
| `float` | Decimal numbers      | `pi = 3.14`       |
| `str`   | Text (string)        | `name = "Linh"`   |
| `bool`  | Boolean (True/False) | `is_adult = True` |

---

### 📝 You can check the type with:

```python
print(type(age))        # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type("hello"))    # <class 'str'>
```

## ➕ Basic Operations and Expressions

Python supports common math operations:

| Operation      | Symbol | Example        |
| -------------- | ------ | -------------- |
| Addition       | `+`    | `3 + 2 → 5`    |
| Subtraction    | `-`    | `5 - 2 → 3`    |
| Multiplication | `*`    | `4 * 3 → 12`   |
| Division       | `/`    | `10 / 2 → 5.0` |
| Modulus        | `%`    | `5 % 2 → 1`    |
| Power          | `**`   | `2 ** 3 → 8`   |
| Floor Div      | `//`   | `5 // 2 → 2`   |

---

## 🔄 Type Conversion (Casting)

You can convert between types using built-in functions:

| Convert To | Use Function | Example                |
| ---------- | ------------ | ---------------------- |
| Integer    | `int()`      | `int("123") → 123`     |
| Float      | `float()`    | `float("3.14") → 3.14` |
| String     | `str()`      | `str(100) → "100"`     |
| Boolean    | `bool()`     | `bool("") → False`     |

---

### 📝 Examples:

```python
age_str = "21"
age_num = int(age_str)

pi = 3.14
pi_text = str(pi)

print(bool(0))     # False
print(bool("Hi"))  # True
```

## 📝 Assignment 1: BMI Calculator

Write a program that:

- Takes user input for weight (kg) and height (m)
- Calculates the BMI: `BMI = weight / (height ** 2)`
- Prints the BMI result
- Classifies the result:
  - BMI < 18.5: Underweight
  - 18.5 <= BMI < 25: Normal
  - 25 <= BMI < 30: Overweight
  - BMI >= 30: Obese

### ✅ Example:

```python
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
bmi = weight / (height ** 2)
print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You are normal.")
elif bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")
```

---

## 📝 Assignment 2: Currency Converter

Write a program that:

- Asks the user to input an amount in VND
- Converts the amount to USD
- Displays the result using formatted strings

Assume:

- 1 USD = 24,000 VND

### ✅ Example:

```python
vnd = float(input("Enter amount in VND: "))
usd = vnd / 24000
print(f"{vnd} VND is approximately {usd:.2f} USD")
```

---

## 💡 Tips:

- Use `type()` to check variable types.
- Use `round(number, digits)` to round float results.
- Use underscores to make large numbers more readable: `24000` → `24_000`.

---

Contact me anytime when you have the problem: anatwork14@gmail.com
