# Day 36: Advanced Linked List Problems

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:

    def __init__(self):
        self.head = None

    # Q1: Insert at end
    def insert_end(self, data):

        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Q2: Display linked list
    def display(self):

        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # Q3: Insert at beginning
    def insert_begin(self, data):

        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    # Q4: Delete by value
    def delete_value(self, value):

        temp = self.head

        if temp and temp.data == value:
            self.head = temp.next
            return

        prev = None

        while temp and temp.data != value:
            prev = temp
            temp = temp.next

        if temp:
            prev.next = temp.next

    # Q5: Find length
    def length(self):

        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count

    # Q6: Find nth node
    def nth_node(self, n):

        temp = self.head
        count = 1

        while temp:

            if count == n:
                return temp.data

            count += 1
            temp = temp.next

        return None

    # Q7: Detect loop
    def detect_loop(self):

        slow = self.head
        fast = self.head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    # Q8: Remove duplicates
    def remove_duplicates(self):

        seen = set()

        temp = self.head
        prev = None

        while temp:

            if temp.data in seen:
                prev.next = temp.next

            else:
                seen.add(temp.data)
                prev = temp

            temp = temp.next

    # Q9: Reverse linked list
    def reverse(self):

        prev = None
        current = self.head

        while current:

            next_node = current.next
            current.next = prev

            prev = current
            current = next_node

        self.head = prev

# Create linked list
ll = LinkedList()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(20)
ll.insert_end(30)

print("Original Linked List:")
ll.display()

print("---------------------------")

# Insert at beginning
ll.insert_begin(5)

print("After inserting at beginning:")
ll.display()

print("---------------------------")

# Delete value
ll.delete_value(20)

print("After deleting 20:")
ll.display()

print("---------------------------")

# Length
print("Length:", ll.length())

print("---------------------------")

# Nth node
n = int(input("Enter node position: "))

print("Nth node:", ll.nth_node(n))

print("---------------------------")

# Loop detection
print("Loop detected:", ll.detect_loop())

print("---------------------------")

# Remove duplicates
ll.remove_duplicates()

print("After removing duplicates:")
ll.display()

print("---------------------------")

# Reverse linked list
ll.reverse()

print("Reversed Linked List:")
ll.display()

print("---------------------------")

# Q10: Merge two linked lists
ll2 = LinkedList()

ll2.insert_end(100)
ll2.insert_end(200)

temp = ll.head

while temp.next:
    temp = temp.next

temp.next = ll2.head

print("Merged Linked List:")
ll.display()
