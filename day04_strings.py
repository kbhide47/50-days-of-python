# Day 04: Strings Practice

# Q1: Take a string and print it
text = input("Enter a string: ")
print("You entered:", text)

print("---------------------------")

# Q2: Print string in uppercase and lowercase
text = input("Enter a string: ")
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

print("---------------------------")

# Q3: Find length of string
text = input("Enter a string: ")
print("Length:", len(text))

print("---------------------------")

# Q4: Reverse a string
text = input("Enter a string: ")
print("Reversed:", text[::-1])

print("---------------------------")

# Q5: Check if string is palindrome
text = input("Enter a string: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

print("---------------------------")

# Q6: Count vowels in a string
text = input("Enter a string: ")
count = 0
for ch in text.lower():
    if ch in 'aeiou':
        count += 1
print("Number of vowels:", count)

print("---------------------------")

# Q7: Replace spaces with hyphens
text = input("Enter a string: ")
print("Modified:", text.replace(" ", "-"))

print("---------------------------")

# Q8: Check if substring exists
text = input("Enter main string: ")
sub = input("Enter substring: ")

if sub in text:
    print("Substring found")
else:
    print("Substring not found")

print("---------------------------")

# Q9: Count frequency of a character
text = input("Enter a string: ")
ch = input("Enter a character to count: ")

count = text.count(ch)
print("Frequency:", count)

print("---------------------------")

# Q10: Remove all spaces from string
text = input("Enter a string: ")
print("Without spaces:", text.replace(" ", ""))
