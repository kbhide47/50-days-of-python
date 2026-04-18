# Day 03: Conditions (if-else)

# Q1: Positive, Negative or Zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

print("---------------------------")

# Q2: Largest of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest is:", a)
else:
    print("Largest is:", b)

print("---------------------------")

# Q3: Largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest is:", a)
elif b >= c:
    print("Largest is:", b)
else:
    print("Largest is:", c)

print("---------------------------")

# Q4: Divisible by 5
num = int(input("Enter a number: "))
if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

print("---------------------------")

# Q5: Divisible by 2 and 3
num = int(input("Enter a number: "))
if num % 2 == 0 and num % 3 == 0:
    print("Divisible by both 2 and 3")
else:
    print("Not divisible by both")

print("---------------------------")

# Q6: Voting eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

print("---------------------------")

# Q7: Vowel or Consonant
ch = input("Enter a character: ")
if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")

print("---------------------------")

# Q8: Pass or Fail
marks = int(input("Enter marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")

print("---------------------------")

# Q9: Grade system
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Grade D")

print("---------------------------")

# Q10: Simple Calculator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    print("Result:", a / b)
else:
    print("Invalid operator")
