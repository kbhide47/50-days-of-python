# Day 31: Problem Solving Practice

# Q1: Find maximum occurring element
numbers = list(map(int, input("Enter numbers: ").split()))

freq = {}

for num in numbers:
    freq[num] = freq.get(num, 0) + 1

max_element = max(freq, key=freq.get)

print("Maximum occurring element:", max_element)

print("---------------------------")

# Q2: Find unique elements
numbers = list(map(int, input("Enter numbers: ").split()))

unique = []

for num in numbers:
    if numbers.count(num) == 1:
        unique.append(num)

print("Unique elements:", unique)

print("---------------------------")

# Q3: Rotate list left by 1
numbers = list(map(int, input("Enter numbers: ").split()))

rotated = numbers[1:] + numbers[:1]

print("Left rotated list:", rotated)

print("---------------------------")

# Q4: Find largest palindrome word
sentence = input("Enter sentence: ").split()

palindromes = []

for word in sentence:
    if word == word[::-1]:
        palindromes.append(word)

if palindromes:
    largest = max(palindromes, key=len)
    print("Largest palindrome word:", largest)
else:
    print("No palindrome words")

print("---------------------------")

# Q5: Find pairs with given sum
numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target sum: "))

pairs = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            pairs.append((numbers[i], numbers[j]))

print("Pairs:", pairs)

print("---------------------------")

# Q6: Reverse words in sentence
sentence = input("Enter sentence: ")

words = sentence.split()

reversed_sentence = " ".join(words[::-1])

print("Reversed sentence:", reversed_sentence)

print("---------------------------")

# Q7: Find longest word
sentence = input("Enter sentence: ").split()

longest = max(sentence, key=len)

print("Longest word:", longest)

print("---------------------------")

# Q8: Count vowels in each word
sentence = input("Enter sentence: ").split()

for word in sentence:
    count = 0

    for ch in word.lower():
        if ch in "aeiou":
            count += 1

    print(word, "->", count)

print("---------------------------")

# Q9: Find intersection without set
list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

intersection = []

for num in list1:
    if num in list2 and num not in intersection:
        intersection.append(num)

print("Intersection:", intersection)

print("---------------------------")

# Q10: Mini inventory system
inventory = {}

n = int(input("How many products? "))

for i in range(n):
    product = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))

    inventory[product] = quantity

print("Inventory:")

for product, quantity in inventory.items():
    print(product, ":", quantity)
