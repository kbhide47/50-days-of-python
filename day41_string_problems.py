# Day 41: String Interview Problems

# Q1: Reverse a string
text = input("Enter a string: ")

print("Reversed String:", text[::-1])

print("---------------------------")

# Q2: Check palindrome
text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

print("---------------------------")

# Q3: Count vowels and consonants
text = input("Enter a string: ").lower()

vowels = consonants = 0

for ch in text:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)

print("---------------------------")

# Q4: Remove spaces
text = input("Enter a string: ")

print("Without spaces:", text.replace(" ", ""))

print("---------------------------")

# Q5: Count frequency of characters
text = input("Enter a string: ")

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print("Character Frequency:", freq)

print("---------------------------")

# Q6: Find first non-repeating character
text = input("Enter a string: ")

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

for ch in text:
    if freq[ch] == 1:
        print("First Non-Repeating Character:", ch)
        break
else:
    print("No unique character found")

print("---------------------------")

# Q7: Check anagram
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1.lower()) == sorted(s2.lower()):
    print("Anagram")
else:
    print("Not Anagram")

print("---------------------------")

# Q8: Find longest word in sentence
sentence = input("Enter sentence: ").split()

longest = max(sentence, key=len)

print("Longest Word:", longest)

print("---------------------------")

# Q9: Capitalize first letter of each word
sentence = input("Enter sentence: ")

print("Capitalized:", sentence.title())

print("---------------------------")

# Q10: Count words in sentence
sentence = input("Enter sentence: ")

words = sentence.split()

print("Total Words:", len(words))
