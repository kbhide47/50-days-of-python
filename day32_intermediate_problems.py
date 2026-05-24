# Day 32: Intermediate Problem Solving

# Q1: Find first repeating element
numbers = list(map(int, input("Enter numbers: ").split()))

seen = set()
found = False

for num in numbers:
    if num in seen:
        print("First repeating element:", num)
        found = True
        break

    seen.add(num)

if not found:
    print("No repeating element")

print("---------------------------")

# Q2: Find first non-repeating character
text = input("Enter string: ")

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

for ch in text:
    if freq[ch] == 1:
        print("First non-repeating character:", ch)
        break
else:
    print("No unique character")

print("---------------------------")

# Q3: Merge two sorted lists
list1 = sorted(list(map(int, input("Enter first sorted list: ").split())))
list2 = sorted(list(map(int, input("Enter second sorted list: ").split())))

merged = []
i = j = 0

while i < len(list1) and j < len(list2):

    if list1[i] < list2[j]:
        merged.append(list1[i])
        i += 1
    else:
        merged.append(list2[j])
        j += 1

while i < len(list1):
    merged.append(list1[i])
    i += 1

while j < len(list2):
    merged.append(list2[j])
    j += 1

print("Merged list:", merged)

print("---------------------------")

# Q4: Find missing characters from alphabet
text = input("Enter string: ").lower()

alphabet = "abcdefghijklmnopqrstuvwxyz"

missing = []

for ch in alphabet:
    if ch not in text:
        missing.append(ch)

print("Missing characters:", missing)

print("---------------------------")

# Q5: Find duplicates in string
text = input("Enter string: ")

duplicates = []

for ch in text:
    if text.count(ch) > 1 and ch not in duplicates:
        duplicates.append(ch)

print("Duplicate characters:", duplicates)

print("---------------------------")

# Q6: Check if arrays are equal
list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

if sorted(list1) == sorted(list2):
    print("Arrays are equal")
else:
    print("Arrays are not equal")

print("---------------------------")

# Q7: Find leaders in array
numbers = list(map(int, input("Enter numbers: ").split()))

leaders = []

max_right = numbers[-1]

leaders.append(max_right)

for i in range(len(numbers) - 2, -1, -1):

    if numbers[i] > max_right:
        max_right = numbers[i]
        leaders.append(max_right)

leaders.reverse()

print("Leaders:", leaders)

print("---------------------------")

# Q8: Remove common elements from two lists
list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

result1 = [x for x in list1 if x not in list2]
result2 = [x for x in list2 if x not in list1]

print("Unique elements:", result1 + result2)

print("---------------------------")

# Q9: Find word with highest frequency
sentence = input("Enter sentence: ").split()

freq = {}

for word in sentence:
    freq[word] = freq.get(word, 0) + 1

max_word = max(freq, key=freq.get)

print("Highest frequency word:", max_word)

print("---------------------------")

# Q10: Mini expense tracker
expenses = {}

n = int(input("How many expenses? "))

for i in range(n):
    item = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expenses[item] = amount

total = sum(expenses.values())

print("Expenses:")

for item, amount in expenses.items():
    print(item, ":", amount)

print("Total Expense:", total)
