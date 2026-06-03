# Day 42: Stack and Queue Interview Problems

from collections import deque

# Q1: Implement Stack using List
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

print("---------------------------")

# Q2: Pop from Stack
if stack:
    print("Popped:", stack.pop())

print("Stack after pop:", stack)

print("---------------------------")

# Q3: Reverse a String using Stack
text = input("Enter string: ")

stack = list(text)

reversed_text = ""

while stack:
    reversed_text += stack.pop()

print("Reversed String:", reversed_text)

print("---------------------------")

# Q4: Check Balanced Parentheses
expression = input("Enter expression: ")

stack = []
balanced = True

for ch in expression:

    if ch == "(":
        stack.append(ch)

    elif ch == ")":

        if stack:
            stack.pop()
        else:
            balanced = False
            break

if stack:
    balanced = False

if balanced:
    print("Balanced")
else:
    print("Not Balanced")

print("---------------------------")

# Q5: Implement Queue using deque
queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", list(queue))

print("---------------------------")

# Q6: Remove from Queue
if queue:
    print("Removed:", queue.popleft())

print("Queue after removal:", list(queue))

print("---------------------------")

# Q7: Generate Binary Numbers from 1 to N
n = int(input("Enter N: "))

queue = deque(["1"])

for i in range(n):

    current = queue.popleft()

    print(current, end=" ")

    queue.append(current + "0")
    queue.append(current + "1")

print()

print("---------------------------")

# Q8: Check Palindrome using Stack
text = input("Enter string: ")

stack = list(text)

reversed_text = ""

while stack:
    reversed_text += stack.pop()

if text == reversed_text:
    print("Palindrome")
else:
    print("Not Palindrome")

print("---------------------------")

# Q9: Next Greater Element
arr = list(map(int, input("Enter numbers: ").split()))

result = []

for i in range(len(arr)):

    next_greater = -1

    for j in range(i + 1, len(arr)):

        if arr[j] > arr[i]:
            next_greater = arr[j]
            break

    result.append(next_greater)

print("Next Greater Elements:", result)

print("---------------------------")

# Q10: Browser History Simulation
history = []

history.append("Google")
history.append("YouTube")
history.append("GitHub")

print("History:", history)

history.pop()

print("After Back Button:", history)

print("Current Page:", history[-1])
