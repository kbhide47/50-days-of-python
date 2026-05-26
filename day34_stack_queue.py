# Day 34: Stack and Queue Problems

from collections import deque

# Q1: Stack push operation
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after push:", stack)

print("---------------------------")

# Q2: Stack pop operation
if stack:
    removed = stack.pop()
    print("Popped element:", removed)

print("Stack:", stack)

print("---------------------------")

# Q3: Reverse string using stack
text = input("Enter string: ")

stack = []

for ch in text:
    stack.append(ch)

reversed_text = ""

while stack:
    reversed_text += stack.pop()

print("Reversed string:", reversed_text)

print("---------------------------")

# Q4: Check balanced parentheses
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

# Q5: Queue operations
queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", list(queue))

removed = queue.popleft()

print("Removed:", removed)
print("Queue after removal:", list(queue))

print("---------------------------")

# Q6: Generate Fibonacci using queue
queue = deque([0, 1])

n = int(input("Enter number of terms: "))

print(0, 1, end=" ")

for i in range(n - 2):

    next_num = queue[0] + queue[1]

    print(next_num, end=" ")

    queue.popleft()
    queue.append(next_num)

print()

print("---------------------------")

# Q7: Find next greater element
numbers = list(map(int, input("Enter numbers: ").split()))

result = []

for i in range(len(numbers)):

    next_greater = -1

    for j in range(i + 1, len(numbers)):

        if numbers[j] > numbers[i]:
            next_greater = numbers[j]
            break

    result.append(next_greater)

print("Next greater elements:", result)

print("---------------------------")

# Q8: Remove duplicates using stack logic
text = input("Enter string: ")

stack = []

for ch in text:

    if not stack or stack[-1] != ch:
        stack.append(ch)

print("Result:", "".join(stack))

print("---------------------------")

# Q9: Circular queue simulation
queue = deque(maxlen=3)

queue.append(1)
queue.append(2)
queue.append(3)

print("Queue:", list(queue))

queue.append(4)

print("After adding 4:", list(queue))

print("---------------------------")

# Q10: Browser history simulation
history = []

history.append("Google")
history.append("YouTube")
history.append("GitHub")

print("Current history:", history)

print("Back button pressed")

history.pop()

print("Now at:", history[-1])
