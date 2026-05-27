# Day 35: Linked List Basics

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Q1: Create single node
node1 = Node(10)

print("Node data:", node1.data)

print("---------------------------")

# Q2: Create linked list manually
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

print("Linked list created")

print("---------------------------")

# Q3: Traverse linked list
temp = node1

print("Linked List:")

while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")

print("---------------------------")

# Q4: Insert at beginning
new_node = Node(5)

new_node.next = node1
head = new_node

temp = head

print("After insertion at beginning:")

while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")

print("---------------------------")

# Q5: Insert at end
new_node = Node(40)

temp = head

while temp.next:
    temp = temp.next

temp.next = new_node

temp = head

print("After insertion at end:")

while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")

print("---------------------------")

# Q6: Count nodes
count = 0

temp = head

while temp:
    count += 1
    temp = temp.next

print("Total nodes:", count)

print("---------------------------")

# Q7: Search element
target = int(input("Enter element to search: "))

temp = head
found = False

while temp:

    if temp.data == target:
        found = True
        break

    temp = temp.next

if found:
    print("Element found")
else:
    print("Element not found")

print("---------------------------")

# Q8: Delete first node
head = head.next

temp = head

print("After deleting first node:")

while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")

print("---------------------------")

# Q9: Reverse linked list
prev = None
current = head

while current:

    next_node = current.next
    current.next = prev

    prev = current
    current = next_node

head = prev

temp = head

print("Reversed Linked List:")

while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")

print("---------------------------")

# Q10: Find middle node
slow = head
fast = head

while fast and fast.next:

    slow = slow.next
    fast = fast.next.next

print("Middle node:", slow.data)
