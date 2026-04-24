# Day 07: Pattern Printing (Loops Mastery)

# Q1: Print square pattern
n = int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

print("---------------------------")

# Q2: Right-angled triangle
n = int(input("Enter n: "))
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("---------------------------")

# Q3: Inverted triangle
n = int(input("Enter n: "))
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

print("---------------------------")

# Q4: Pyramid pattern
n = int(input("Enter n: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("* " * i)

print("---------------------------")

# Q5: Number pattern
n = int(input("Enter n: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("---------------------------")

# Q6: Same number pattern
n = int(input("Enter n: "))
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()

print("---------------------------")

# Q7: Reverse number pattern
n = int(input("Enter n: "))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("---------------------------")

# Q8: Alphabet pattern
n = int(input("Enter n: "))
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()

print("---------------------------")

# Q9: Floyd’s triangle
n = int(input("Enter n: "))
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

print("---------------------------")

# Q10: Hollow square pattern
n = int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
