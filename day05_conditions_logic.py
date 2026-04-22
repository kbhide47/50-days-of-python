# Day 05: Condition-Based Problems (Logic Building)

# Q1: Check leap year
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

print("---------------------------")

# Q2: Check if number is multiple of 7
num = int(input("Enter a number: "))
if num % 7 == 0:
    print("Multiple of 7")
else:
    print("Not a multiple of 7")

print("---------------------------")

# Q3: Find smallest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a <= b and a <= c:
    print("Smallest is:", a)
elif b <= c:
    print("Smallest is:", b)
else:
    print("Smallest is:", c)

print("---------------------------")

# Q4: Electricity bill (simple logic)
units = int(input("Enter units consumed: "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
else:
    bill = units * 10
print("Total bill:", bill)

print("---------------------------")

# Q5: Check if character is alphabet, digit or special character
ch = input("Enter a character: ")
if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")

print("---------------------------")

# Q6: Check profit or loss
cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))
if sp > cp:
    print("Profit")
elif sp < cp:
    print("Loss")
else:
    print("No Profit No Loss")

print("---------------------------")

# Q7: Check if number is 3-digit
num = int(input("Enter a number: "))
if 100 <= num <= 999:
    print("3-digit number")
else:
    print("Not a 3-digit number")

print("---------------------------")

# Q8: Calculate bonus based on salary
salary = float(input("Enter salary: "))
if salary > 50000:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05
print("Bonus:", bonus)

print("---------------------------")

# Q9: Check if number is divisible by 2, 3 or both
num = int(input("Enter a number: "))
if num % 2 == 0 and num % 3 == 0:
    print("Divisible by both 2 and 3")
elif num % 2 == 0:
    print("Divisible by 2 only")
elif num % 3 == 0:
    print("Divisible by 3 only")
else:
    print("Not divisible by 2 or 3")

print("---------------------------")

# Q10: Simple menu-driven calculator
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
choice = int(input("Enter your choice: "))

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    print("Result:", a + b)
elif choice == 2:
    print("Result:", a - b)
elif choice == 3:
    print("Result:", a * b)
elif choice == 4:
    print("Result:", a / b)
else:
    print("Invalid choice")
