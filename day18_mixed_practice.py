# Day 18: Mixed Practice Problems

# Q1: Find sum of even numbers in list
lst = list(map(int, input("Enter numbers: ").split()))
even_sum = 0

for num in lst:
    if num % 2 == 0:
        even_sum += num

print("Sum of even numbers:", even_sum)

print("---------------------------")

# Q2: Find largest word in sentence
sentence = input("Enter a sentence: ").split()
largest = max(sentence, key=len)
print("Largest word:", largest)

print("---------------------------")

# Q3: Count positive, negative and zero
lst = list(map(int, input("Enter numbers: ").split()))

positive = negative = zero = 0

for num in lst:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)

print("---------------------------")

# Q4: Find common characters in two strings
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

common = set(s1) & set(s2)

print("Common characters:", common)

print("---------------------------")

# Q5: Remove duplicates from string
text = input("Enter a string: ")
result = ""

for ch in text:
    if ch not in result:
        result += ch

print("Without duplicates:", result)

print("---------------------------")

# Q6: Check Armstrong number
num = int(input("Enter a number: "))
temp = num
digits = len(str(num))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == num:
    print("Armstrong Number")
else:
    print("Not Armstrong")

print("---------------------------")

# Q7: Find factorial using function
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

n = int(input("Enter a number: "))
print("Factorial:", factorial(n))

print("---------------------------")

# Q8: Merge two dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

merged = d1 | d2

print("Merged dictionary:", merged)

print("---------------------------")

# Q9: Find second smallest number
lst = list(map(int, input("Enter numbers: ").split()))

unique = sorted(set(lst))

if len(unique) >= 2:
    print("Second smallest:", unique[1])
else:
    print("Not possible")

print("---------------------------")

# Q10: Print prime numbers from 1 to n
n = int(input("Enter n: "))

for num in range(2, n + 1):
    prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, end=" ")
