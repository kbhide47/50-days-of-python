# Day 06: Loops Practice (for & while)

# Q1: Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

print("---------------------------")

# Q2: Print numbers from 10 to 1
for i in range(10, 0, -1):
    print(i)

print("---------------------------")

# Q3: Print even numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

print("---------------------------")

# Q4: Sum of numbers from 1 to n
n = int(input("Enter n: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("Sum is:", sum)

print("---------------------------")

# Q5: Factorial of a number
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)

print("---------------------------")

# Q6: Multiplication table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

print("---------------------------")

# Q7: Count digits in a number
num = int(input("Enter a number: "))
count = 0
temp = num

while temp != 0:
    temp //= 10
    count += 1

print("Number of digits:", count)

print("---------------------------")

# Q8: Reverse a number
num = int(input("Enter a number: "))
rev = 0

while num != 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed number:", rev)

print("---------------------------")

# Q9: Check if number is palindrome
num = int(input("Enter a number: "))
temp = num
rev = 0

while temp != 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if num == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

print("---------------------------")

# Q10: Fibonacci series (first n terms)
n = int(input("Enter number of terms: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
