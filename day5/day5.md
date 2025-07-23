# 📘 Day 5 – Functions

**Main Topics:**

- Defining and calling functions using `def`
- Function parameters and arguments
- Returning values with `return`
- Function structure and reusability

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Define your own functions using `def`
- Pass input values (parameters) to functions
- Return results from a function
- Use functions to organize and reuse code

---

## 🧩 Function Basics

### ✅ Syntax:

```python
def function_name(parameters):
    # code block
    return result
```

### 📝 Example:

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Linh"))  # Hello, Linh!
```

---

## 📝 Assignment 1: Prime Number Checker

Write a function that:

- Accepts a number
- Returns `True` if the number is prime, `False` otherwise

### ✅ Example:

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test
num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
```

---

## 📝 Assignment 2: Factorial Calculator

Write a function that:

- Accepts a non-negative integer
- Returns the factorial of that number

### ✅ Example:

```python
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = int(input("Enter a number: "))
print("Factorial of", n, "is", factorial(n))
```

---

## 📝 Assignment 3: Leap Year Checker

Write a function that:

- Accepts a year as input
- Returns `True` if it is a leap year, `False` otherwise

### ✅ Rules:

- Divisible by 4 → leap year
- Except divisible by 100 → not leap year
- But divisible by 400 → still leap year

### ✅ Example:

```python
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

year = int(input("Enter a year: "))
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
```

---

## 💡 Tips:

- Use `return` to get results from functions
- Keep your functions focused on a single task
- You can reuse functions in larger programs later

---

Contact me anytime when you have the problem: [anatwork14@gmail.com](mailto:anatwork14@gmail.com)
