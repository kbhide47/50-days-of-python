# Day 08: Functions Practice

# Q1: Function to print hello
def greet():
    print("Hello!")

greet()

print("---------------------------")

# Q2: Function to add two numbers
def add(a, b):
    return a + b

print("Sum:", add(5, 3))

print("---------------------------")

# Q3: Function to find square
def square(num):
    return num * num

n = int(input("Enter a number: "))
print("Square:", square(n))

print("---------------------------")

# Q4: Function to check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter a number: "))
print(check_even_odd(n))

print("---------------------------")

# Q5: Function to find factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

n = int(input("Enter a number: "))
print("Factorial:", factorial(n))

print("---------------------------")

# Q6: Function to find largest of three numbers
def largest(a, b, c):
    return max(a, b, c)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Largest:", largest(a, b, c))

print("---------------------------")

# Q7: Function to count vowels in string
def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count

text = input("Enter a string: ")
print("Vowels:", count_vowels(text))

print("---------------------------")

# Q8: Function to reverse string
def reverse_string(text):
    return text[::-1]

text = input("Enter a string: ")
print("Reversed:", reverse_string(text))

print("---------------------------")

# Q9: Function to check palindrome
def is_palindrome(text):
    return text == text[::-1]

text = input("Enter a string: ")
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")

print("---------------------------")

# Q10: Function for simple calculator
def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        return "Invalid operator"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")
print("Result:", calculator(a, b, op))
