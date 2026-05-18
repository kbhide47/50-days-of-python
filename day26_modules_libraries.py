# Day 26: Modules and Libraries Practice

# Q1: Square root using math module
import math

num = int(input("Enter number: "))

print("Square root:", math.sqrt(num))

print("---------------------------")

# Q2: Power function
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

print("Power:", math.pow(base, exp))

print("---------------------------")

# Q3: Find factorial using math module
num = int(input("Enter number: "))

print("Factorial:", math.factorial(num))

print("---------------------------")

# Q4: Generate random number
import random

print("Random number:", random.randint(1, 100))

print("---------------------------")

# Q5: Random choice from list
colors = ["Red", "Blue", "Green", "Black"]

print("Random color:", random.choice(colors))

print("---------------------------")

# Q6: Shuffle list
numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print("Shuffled list:", numbers)

print("---------------------------")

# Q7: Current date and time
import datetime

now = datetime.datetime.now()

print("Current date and time:", now)

print("---------------------------")

# Q8: Display only current date
today = datetime.date.today()

print("Today's date:", today)

print("---------------------------")

# Q9: Get current working directory
import os

print("Current directory:", os.getcwd())

print("---------------------------")

# Q10: List files in current directory
files = os.listdir()

print("Files and folders:")

for file in files:
    print(file)
