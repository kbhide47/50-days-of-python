# Day 11: String Problems (Logic Building)

# Q1: Count uppercase and lowercase letters
text = input("Enter a string: ")
upper = lower = 0

for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase:", upper)
print("Lowercase:", lower)

print("---------------------------")

# Q2: Count digits in a string
text = input("Enter a string: ")
count = 0

for ch in text:
    if ch.isdigit():
        count += 1

print("Digits:", count)

print("---------------------------")

# Q3: Remove all vowels
text = input("Enter a string: ")
result = ""

for ch in text:
    if ch.lower() not in "aeiou":
        result += ch

print("Without vowels:", result)

print("---------------------------")

# Q4: Check anagram
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")

print("---------------------------")

# Q5: Count words in a sentence
text = input("Enter a sentence: ")
words = text.split()
print("Number of words:", len(words))

print("---------------------------")

# Q6: Find frequency of each character
text = input("Enter a string: ")
freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print("Frequency:", freq)

print("---------------------------")

# Q7: Remove duplicate characters
text = input("Enter a string: ")
result = ""

for ch in text:
    if ch not in result:
        result += ch

print("Without duplicates:", result)

print("---------------------------")

# Q8: Find largest word in sentence
text = input("Enter a sentence: ")
words = text.split()
largest = max(words, key=len)
print("Largest word:", largest)

print("---------------------------")

# Q9: Capitalize first letter of each word
text = input("Enter a sentence: ")
print("Capitalized:", text.title())

print("---------------------------")

# Q10: Check if string contains only alphabets
text = input("Enter a string: ")

if text.isalpha():
    print("Only alphabets")
else:
    print("Contains other characters")
