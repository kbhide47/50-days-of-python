# Day 27: Functions and Recursion

# Q1: Simple recursive countdown
def countdown(n):
    if n == 0:
        print("Done")
        return

    print(n)
    countdown(n - 1)

countdown(5)

print("---------------------------")

# Q2: Recursive factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

num = int(input("Enter number: "))

print("Factorial:", factorial(num))

print("---------------------------")

# Q3: Recursive Fibonacci
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter term number: "))

print("Fibonacci:", fibonacci(n))

print("---------------------------")

# Q4: Sum of numbers using recursion
def total(n):
    if n == 1:
        return 1

    return n + total(n - 1)

num = int(input("Enter number: "))

print("Sum:", total(num))

print("---------------------------")

# Q5: Power using recursion
def power(base, exp):
    if exp == 0:
        return 1

    return base * power(base, exp - 1)

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

print("Power:", power(base, exp))

print("---------------------------")

# Q6: Reverse string using recursion
def reverse_string(text):
    if len(text) == 0:
        return text

    return reverse_string(text[1:]) + text[0]

text = input("Enter string: ")

print("Reversed:", reverse_string(text))

print("---------------------------")

# Q7: Check palindrome using recursion
def palindrome(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return palindrome(text[1:-1])

text = input("Enter string: ")

if palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")

print("---------------------------")

# Q8: Lambda function
square = lambda x: x * x

num = int(input("Enter number: "))

print("Square:", square(num))

print("---------------------------")

# Q9: Map function
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print("Squares:", squares)

print("---------------------------")

# Q10: Filter function
numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", even)
