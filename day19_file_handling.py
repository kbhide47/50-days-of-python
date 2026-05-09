# Day 19: File Handling Practice

# Q1: Create and write to a file
file = open("sample.txt", "w")
file.write("Hello, this is Day 19.\n")
file.write("Learning File Handling in Python.")
file.close()

print("Data written successfully")

print("---------------------------")

# Q2: Read entire file
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

print("---------------------------")

# Q3: Read file line by line
file = open("sample.txt", "r")

for line in file:
    print(line.strip())

file.close()

print("---------------------------")

# Q4: Append data to file
file = open("sample.txt", "a")
file.write("\nThis line is appended.")
file.close()

print("Data appended successfully")

print("---------------------------")

# Q5: Count number of words in file
file = open("sample.txt", "r")
content = file.read()

words = content.split()

print("Number of words:", len(words))

file.close()

print("---------------------------")

# Q6: Count number of lines in file
file = open("sample.txt", "r")

lines = file.readlines()

print("Number of lines:", len(lines))

file.close()

print("---------------------------")

# Q7: Count vowels in file
file = open("sample.txt", "r")
content = file.read().lower()

count = 0

for ch in content:
    if ch in "aeiou":
        count += 1

print("Number of vowels:", count)

file.close()

print("---------------------------")

# Q8: Copy content from one file to another
source = open("sample.txt", "r")
data = source.read()

target = open("copy.txt", "w")
target.write(data)

source.close()
target.close()

print("File copied successfully")

print("---------------------------")

# Q9: Search a word in file
word = input("Enter word to search: ")

file = open("sample.txt", "r")
content = file.read()

if word in content:
    print("Word found")
else:
    print("Word not found")

file.close()

print("---------------------------")

# Q10: Display file size
import os

size = os.path.getsize("sample.txt")

print("File size:", size, "bytes")
