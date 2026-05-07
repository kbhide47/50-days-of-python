# Day 17: Dictionaries Practice

# Q1: Create a dictionary and print it
student = {
    "name": "Kasturi",
    "age": 20,
    "branch": "ENTC"
}

print("Dictionary:", student)

print("---------------------------")

# Q2: Access dictionary values
print("Name:", student["name"])
print("Age:", student["age"])

print("---------------------------")

# Q3: Add new key-value pair
student["college"] = "DY Patil"
print("Updated dictionary:", student)

print("---------------------------")

# Q4: Update a value
student["age"] = 21
print("After update:", student)

print("---------------------------")

# Q5: Remove a key
student.pop("branch")
print("After removing branch:", student)

print("---------------------------")

# Q6: Check if key exists
key = input("Enter key to check: ")

if key in student:
    print("Key exists")
else:
    print("Key does not exist")

print("---------------------------")

# Q7: Iterate through dictionary
for key, value in student.items():
    print(key, ":", value)

print("---------------------------")

# Q8: Count frequency of elements in list
lst = list(map(int, input("Enter numbers: ").split()))
freq = {}

for num in lst:
    freq[num] = freq.get(num, 0) + 1

print("Frequency dictionary:", freq)

print("---------------------------")

# Q9: Find character frequency in string
text = input("Enter a string: ")
char_freq = {}

for ch in text:
    char_freq[ch] = char_freq.get(ch, 0) + 1

print("Character frequency:", char_freq)

print("---------------------------")

# Q10: Find word frequency in sentence
sentence = input("Enter a sentence: ").split()
word_freq = {}

for word in sentence:
    word_freq[word] = word_freq.get(word, 0) + 1

print("Word frequency:", word_freq)
