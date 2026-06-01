# Day 40: Hashing and Array Problems

# Q1: Find frequency of elements
numbers = list(map(int, input("Enter numbers: ").split()))

freq = {}

for num in numbers:
    freq[num] = freq.get(num, 0) + 1

print("Frequency:", freq)

print("---------------------------")

# Q2: Find element with highest frequency
max_element = max(freq, key=freq.get)

print("Highest frequency element:", max_element)

print("---------------------------")

# Q3: Find duplicates using set
numbers = list(map(int, input("Enter numbers: ").split()))

seen = set()
duplicates = set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Duplicates:", list(duplicates))

print("---------------------------")

# Q4: Check if two strings are anagrams
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")

print("---------------------------")

# Q5: Find first repeating element
numbers = list(map(int, input("Enter numbers: ").split()))

seen = set()

for num in numbers:
    if num in seen:
        print("First repeating element:", num)
        break
    seen.add(num)
else:
    print("No repeating element")

print("---------------------------")

# Q6: Find first non-repeating element
numbers = list(map(int, input("Enter numbers: ").split()))

freq = {}

for num in numbers:
    freq[num] = freq.get(num, 0) + 1

for num in numbers:
    if freq[num] == 1:
        print("First non-repeating element:", num)
        break
else:
    print("No non-repeating element")

print("---------------------------")

# Q7: Two Sum Problem
numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

seen = {}

for i in range(len(numbers)):
    complement = target - numbers[i]

    if complement in seen:
        print("Indices:", seen[complement], i)
        break

    seen[numbers[i]] = i
else:
    print("No pair found")

print("---------------------------")

# Q8: Intersection of two arrays
arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))

intersection = list(set(arr1) & set(arr2))

print("Intersection:", intersection)

print("---------------------------")

# Q9: Union of two arrays
union = list(set(arr1) | set(arr2))

print("Union:", union)

print("---------------------------")

# Q10: Longest word in sentence
sentence = input("Enter sentence: ").split()

longest = max(sentence, key=len)

print("Longest word:", longest)
