# Day 43: Linked List Interview Problems

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None

    # Q1: Insert at End
    def insert_end(self, data):

        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Q2: Display Linked List
    def display(self):

        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # Q3: Count Nodes
    def count_nodes(self):

        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count

    # Q4: Search Element
    def search(self, value):

        temp = self.head

        while temp:

            if temp.data == value:
                return True

            temp = temp.next

        return False

    # Q5: Insert at Beginning
    def insert_begin(self, data):

        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    # Q6: Delete First Node
    def delete_first(self):

        if self.head:
            self.head = self.head.next

    # Q7: Find Middle Node
    def find_middle(self):

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    # Q8: Reverse Linked List
    def reverse(self):

        prev = None
        current = self.head

        while current:

            next_node = current.next
            current.next = prev

            prev = current
            current = next_node

        self.head = prev

    # Q9: Find Last Node
    def last_node(self):

        temp = self.head

        while temp.next:
            temp = temp.next

        return temp.data

    # Q10: Sum of Nodes
    def sum_nodes(self):

        total = 0
        temp = self.head

        while temp:
            total += temp.data
            temp = temp.next

        return total


# Create Linked List
ll = LinkedList()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)
ll.insert_end(40)

print("Original Linked List:")
ll.display()

print("---------------------------")

print("Total Nodes:", ll.count_nodes())

print("---------------------------")

value = int(input("Enter value to search: "))

if ll.search(value):
    print("Value Found")
else:
    print("Value Not Found")

print("---------------------------")

ll.insert_begin(5)

print("After Insert at Beginning:")
ll.display()

print("---------------------------")

ll.delete_first()

print("After Deleting First Node:")
ll.display()

print("---------------------------")

print("Middle Node:", ll.find_middle())

print("---------------------------")

ll.reverse()

print("Reversed Linked List:")
ll.display()

print("---------------------------")

print("Last Node:", ll.last_node())

print("---------------------------")

print("Sum of Nodes:", ll.sum_nodes())
