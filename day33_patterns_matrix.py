# Day 33: Pattern and Matrix Problems

# Q1: Star pattern
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print("*" * i)

print("---------------------------")

# Q2: Reverse star pattern
for i in range(n, 0, -1):
    print("*" * i)

print("---------------------------")

# Q3: Number triangle
for i in range(1, n + 1):

    for j in range(1, i + 1):
        print(j, end=" ")

    print()

print("---------------------------")

# Q4: Floyd's triangle
num = 1

for i in range(1, n + 1):

    for j in range(i):
        print(num, end=" ")
        num += 1

    print()

print("---------------------------")

# Q5: Multiplication table
num = int(input("Enter number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

print("---------------------------")

# Q6: Matrix addition
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix1 = []
matrix2 = []

print("Enter first matrix:")

for i in range(rows):
    row = list(map(int, input().split()))
    matrix1.append(row)

print("Enter second matrix:")

for i in range(rows):
    row = list(map(int, input().split()))
    matrix2.append(row)

result = []

for i in range(rows):

    temp = []

    for j in range(cols):
        temp.append(matrix1[i][j] + matrix2[i][j])

    result.append(temp)

print("Matrix Addition:")

for row in result:
    print(row)

print("---------------------------")

# Q7: Matrix transpose
matrix = []

rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))

print("Enter matrix:")

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

transpose = []

for j in range(cols):

    temp = []

    for i in range(rows):
        temp.append(matrix[i][j])

    transpose.append(temp)

print("Transpose:")

for row in transpose:
    print(row)

print("---------------------------")

# Q8: Sum of diagonal elements
matrix = []

n = int(input("Enter size of square matrix: "))

print("Enter matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

diagonal_sum = 0

for i in range(n):
    diagonal_sum += matrix[i][i]

print("Diagonal Sum:", diagonal_sum)

print("---------------------------")

# Q9: Find largest element in matrix
largest = matrix[0][0]

for row in matrix:
    for value in row:
        if value > largest:
            largest = value

print("Largest element:", largest)

print("---------------------------")

# Q10: Count vowels pattern
text = input("Enter string: ")

for ch in text:
    if ch.lower() in "aeiou":
        print(ch, "-> vowel")
    else:
        print(ch, "-> consonant")
