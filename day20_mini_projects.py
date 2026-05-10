# Day 20: Mini Projects Practice

import random
import string

# Q1: Generate random number
print("Random Number:", random.randint(1, 100))

print("---------------------------")

# Q2: Random choice from list
colors = ["Red", "Blue", "Green", "Black"]
print("Random Color:", random.choice(colors))

print("---------------------------")

# Q3: Generate random password
length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)

print("---------------------------")

# Q4: Password strength checker
password = input("Enter password: ")

if len(password) >= 8:
    print("Strong Password")
else:
    print("Weak Password")

print("---------------------------")

# Q5: Number guessing game
secret = random.randint(1, 10)

guess = int(input("Guess number (1-10): "))

if guess == secret:
    print("Correct Guess!")
else:
    print("Wrong Guess")
    print("Correct number was:", secret)

print("---------------------------")

# Q6: Dice simulator
dice = random.randint(1, 6)
print("Dice rolled:", dice)

print("---------------------------")

# Q7: OTP generator
otp = random.randint(1000, 9999)
print("Generated OTP:", otp)

print("---------------------------")

# Q8: Simple contact book
contacts = {}

name = input("Enter contact name: ")
number = input("Enter contact number: ")

contacts[name] = number

print("Saved Contacts:", contacts)

print("---------------------------")

# Q9: Search contact
search = input("Enter contact name to search: ")

if search in contacts:
    print("Number:", contacts[search])
else:
    print("Contact not found")

print("---------------------------")

# Q10: Simple to-do list
tasks = []

n = int(input("How many tasks to add? "))

for i in range(n):
    task = input("Enter task: ")
    tasks.append(task)

print("Your To-Do List:")
for i, task in enumerate(tasks, start=1):
    print(i, ".", task)
