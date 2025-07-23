# Assignment 1:
# Level 1
print("Assignment 1 - Lv1")
print("👋 Hello, world!")
print("My name is Alice.")
print("I am 22 years old.")
print("My hobbies are reading, painting, and hiking.")
print("----------------------------------------------")
# Level 2
print("Assignment 1 - Lv2")
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
hobbies = input("Please enter your hobbies: ")
print("👋 Hello, world!")
print("My name is", name)
print(f"I am {age} years old.")
print("My hobbies are %s." % hobbies)
print("----------------------------------------------")

# Assignment 2: 
print("Assignment 2")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)

if b != 0:
    print("Quotient:", a / b)
else:
    print("Cannot divide by zero.")
