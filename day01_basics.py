# Day 01: Python Basics

# Q1: Print your name
print("Kasturi")

# Q2: Print name and age
name = "Kasturi"
age = 20
print("My name is", name)
print("My age is", age)

# Q3: Take input and print
user_name = input("Enter your name: ")
print("Hello", user_name)

# Q4: Sum of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum is:", a + b)

# Q5: Square of a number
num = int(input("Enter a number: "))
print("Square is:", num * num)

# Q6: Swap two numbers
x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))

x, y = y, x
print("After swapping:")
print("x =", x)
print("y =", y)

# Q7: Basic math operations
p = int(input("Enter first number: "))
q = int(input("Enter second number: "))

print("Addition:", p + q)
print("Subtraction:", p - q)
print("Multiplication:", p * q)
print("Division:", p / q)

# Q8 to Q10 - Combined Program

# Q8: Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

print("---------------------------")

# Q9: Area of Rectangle
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print("Area of rectangle:", area)

print("---------------------------")

# Q10: Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
