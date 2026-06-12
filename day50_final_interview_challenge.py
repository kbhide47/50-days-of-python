# Day 50: Final Mixed Interview Challenge

from collections import deque

# Q1: Two Sum
nums = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

seen = {}

for i in range(len(nums)):

    complement = target - nums[i]

    if complement in seen:
        print("Two Sum Indices:",
              seen[complement], i)
        break

    seen[nums[i]] = i

print("---------------------------")

# Q2: Palindrome String
text = input("Enter string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

print("---------------------------")

# Q3: First Non-Repeating Character
text = input("Enter string: ")

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

for ch in text:

    if freq[ch] == 1:
        print("First Non-Repeating:", ch)
        break

print("---------------------------")

# Q4: Maximum Subarray Sum (Kadane)
arr = list(map(int, input("Enter numbers: ").split()))

current = maximum = arr[0]

for i in range(1, len(arr)):

    current = max(arr[i],
                  current + arr[i])

    maximum = max(maximum,
                  current)

print("Maximum Subarray Sum:",
      maximum)

print("---------------------------")

# Q5: Binary Search
arr = sorted(list(map(int,
          input("Enter sorted numbers: ").split())))

target = int(input("Enter target: "))

left = 0
right = len(arr) - 1

found = False

while left <= right:

    mid = (left + right) // 2

    if arr[mid] == target:
        found = True
        break

    elif target < arr[mid]:
        right = mid - 1

    else:
        left = mid + 1

print("Found:", found)

print("---------------------------")

# Q6: Linked List Traversal

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

temp = head

print("Linked List:")

while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")

print("---------------------------")

# Q7: Binary Tree Inorder

class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)

def inorder(node):

    if node:

        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

print("Tree Inorder:")
inorder(root)

print("\n---------------------------")

# Q8: Graph BFS

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": []
}

visited = set()

queue = deque(["A"])

visited.add("A")

print("BFS:")

while queue:

    node = queue.popleft()

    print(node, end=" ")

    for neighbor in graph[node]:

        if neighbor not in visited:

            visited.add(neighbor)
            queue.append(neighbor)

print()

print("---------------------------")

# Q9: Climbing Stairs DP
n = int(input("Enter stairs: "))

dp = [0] * (n + 1)

dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print("Ways:", dp[n])

print("---------------------------")

# Q10: Frequency Count
nums = list(map(int, input("Enter numbers: ").split()))

freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

print("Frequency Dictionary:")
print(freq)
