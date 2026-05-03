# Day 15: Advanced Patterns

# Q1: Right aligned triangle
n = int(input("Enter n: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

print("---------------------------")

# Q2: Inverted right aligned triangle
n = int(input("Enter n: "))
for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)

print("---------------------------")

# Q3: Full pyramid
n = int(input("Enter n: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * (2*i - 1))

print("---------------------------")

# Q4: Inverted pyramid
n = int(input("Enter n: "))
for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * (2*i - 1))

print("---------------------------")

# Q5: Diamond pattern
n = int(input("Enter n: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * (2*i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * (2*i - 1))

print("---------------------------")

# Q6: Number pyramid
n = int(input("Enter n: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("---------------------------")

# Q7: Palindrome number pattern
n = int(input("Enter n: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i, 0, -1):
        print(j, end="")
    for j in range(2, i + 1):
        print(j, end="")
    print()

print("---------------------------")

# Q8: Hollow pyramid
n = int(input("Enter n: "))
for i in range(1, n + 1):
    for j in range(1, 2*n):
        if j == n-i+1 or j == n+i-1 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("---------------------------")

# Q9: Binary pattern
n = int(input("Enter n: "))
for i in range(1, n + 1):
    num = i % 2
    for j in range(i):
        print(num, end=" ")
        num = 1 - num
    print()

print("---------------------------")

# Q10: Pascal’s triangle
n = int(input("Enter n: "))
for i in range(n):
    print(" " * (n - i), end="")
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()
