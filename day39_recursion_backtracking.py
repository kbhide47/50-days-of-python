# Day 39: Recursion and Backtracking

# Q1: Print numbers from 1 to n using recursion
def print_numbers(n):
    if n == 0:
        return

    print_numbers(n - 1)
    print(n, end=" ")

n = int(input("Enter n: "))
print_numbers(n)

print("\n---------------------------")

# Q2: Sum of digits using recursion
def sum_digits(num):
    if num == 0:
        return 0

    return num % 10 + sum_digits(num // 10)

num = int(input("Enter number: "))
print("Sum of digits:", sum_digits(num))

print("---------------------------")

# Q3: Count digits using recursion
def count_digits(num):
    if num < 10:
        return 1

    return 1 + count_digits(num // 10)

num = int(input("Enter number: "))
print("Digit count:", count_digits(num))

print("---------------------------")

# Q4: Recursive GCD
def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("GCD:", gcd(a, b))

print("---------------------------")

# Q5: Recursive binary search
def binary_search(arr, left, right, target):

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid

    if target < arr[mid]:
        return binary_search(arr, left, mid - 1, target)

    return binary_search(arr, mid + 1, right, target)

arr = [10, 20, 30, 40, 50, 60]

target = int(input("Enter target: "))

result = binary_search(arr, 0, len(arr) - 1, target)

print("Index:", result)

print("---------------------------")

# Q6: Generate all permutations
def permutations(s, answer):

    if len(s) == 0:
        print(answer)
        return

    for i in range(len(s)):
        ch = s[i]
        left = s[:i]
        right = s[i + 1:]

        permutations(left + right, answer + ch)

text = input("Enter string: ")

permutations(text, "")

print("---------------------------")

# Q7: Power using recursion
def power(base, exp):

    if exp == 0:
        return 1

    return base * power(base, exp - 1)

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

print("Power:", power(base, exp))

print("---------------------------")

# Q8: Recursive palindrome check
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

# Q9: Find all subsets
def subsets(arr, current, index):

    if index == len(arr):
        print(current)
        return

    subsets(arr, current, index + 1)

    subsets(arr, current + [arr[index]], index + 1)

arr = [1, 2, 3]

subsets(arr, [], 0)

print("---------------------------")

# Q10: Count ways to climb stairs
def climb(n):

    if n == 0 or n == 1:
        return 1

    return climb(n - 1) + climb(n - 2)

n = int(input("Enter stairs: "))

print("Ways:", climb(n))
