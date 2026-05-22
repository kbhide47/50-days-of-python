# Day 30: DSA and Logic Practice

# Q1: Find duplicate elements
numbers = list(map(int, input("Enter numbers: ").split()))

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicates:", duplicates)

print("---------------------------")

# Q2: Find missing number from 1 to n
numbers = list(map(int, input("Enter numbers: ").split()))

n = len(numbers) + 1

expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)

print("Missing number:", expected_sum - actual_sum)

print("---------------------------")

# Q3: Find second largest element
numbers = list(set(numbers))

numbers.sort()

if len(numbers) >= 2:
    print("Second largest:", numbers[-2])
else:
    print("Not enough elements")

print("---------------------------")

# Q4: Check palindrome string
text = input("Enter string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

print("---------------------------")

# Q5: Count character frequency
text = input("Enter string: ")

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print("Frequency:", freq)

print("---------------------------")

# Q6: Find common elements in two lists
list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

common = list(set(list1) & set(list2))

print("Common elements:", common)

print("---------------------------")

# Q7: Move zeros to end
numbers = list(map(int, input("Enter numbers: ").split()))

result = [x for x in numbers if x != 0]
zeros = [0] * numbers.count(0)

print("Modified list:", result + zeros)

print("---------------------------")

# Q8: Check anagram
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")

print("---------------------------")

# Q9: Find prime numbers from list
numbers = list(map(int, input("Enter numbers: ").split()))

print("Prime numbers:")

for num in numbers:
    if num > 1:
        prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break

        if prime:
            print(num, end=" ")

print()

print("---------------------------")

# Q10: Simple student record system
students = {}

n = int(input("How many students? "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    students[name] = marks

print("Student Records:")

for name, marks in students.items():
    print(name, ":", marks)
