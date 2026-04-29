# Day 12: Advanced String Problems

# Q1: Count vowels, consonants, digits, spaces
text = input("Enter a string: ")
v = c = d = s = 0

for ch in text:
    if ch.lower() in "aeiou":
        v += 1
    elif ch.isalpha():
        c += 1
    elif ch.isdigit():
        d += 1
    elif ch.isspace():
        s += 1

print("Vowels:", v, "Consonants:", c, "Digits:", d, "Spaces:", s)

print("---------------------------")

# Q2: Check if string is a pangram
text = input("Enter a string: ").lower()
alphabet = set("abcdefghijklmnopqrstuvwxyz")

if alphabet.issubset(set(text)):
    print("Pangram")
else:
    print("Not Pangram")

print("---------------------------")

# Q3: Find first non-repeating character
text = input("Enter a string: ")

for ch in text:
    if text.count(ch) == 1:
        print("First non-repeating character:", ch)
        break
else:
    print("No unique character")

print("---------------------------")

# Q4: Replace multiple spaces with single space
text = input("Enter a string: ")
result = " ".join(text.split())
print("Modified:", result)

print("---------------------------")

# Q5: Remove punctuation
import string

text = input("Enter a string: ")
result = ""

for ch in text:
    if ch not in string.punctuation:
        result += ch

print("Without punctuation:", result)

print("---------------------------")

# Q6: Check if two strings are rotations
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("Rotation")
else:
    print("Not Rotation")

print("---------------------------")

# Q7: Count frequency of words
text = input("Enter a sentence: ")
words = text.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Word frequency:", freq)

print("---------------------------")

# Q8: Reverse each word in sentence
text = input("Enter a sentence: ")
words = text.split()
result = []

for word in words:
    result.append(word[::-1])

print("Modified:", " ".join(result))

print("---------------------------")

# Q9: Find longest common prefix
strs = input("Enter words separated by space: ").split()

prefix = strs[0]
for word in strs[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]

print("Longest common prefix:", prefix)

print("---------------------------")

# Q10: Check balanced parentheses
text = input("Enter parentheses string: ")
stack = []

for ch in text:
    if ch == "(":
        stack.append(ch)
    elif ch == ")":
        if stack:
            stack.pop()
        else:
            print("Not Balanced")
            break
else:
    if not stack:
        print("Balanced")
    else:
        print("Not Balanced")
