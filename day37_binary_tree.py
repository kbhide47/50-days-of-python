# Day 37: Binary Tree Basics

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Q1: Create root node
root = Node(10)

print("Root Node:", root.data)

print("---------------------------")

# Q2: Add child nodes
root.left = Node(20)
root.right = Node(30)

print("Left Child:", root.left.data)
print("Right Child:", root.right.data)

print("---------------------------")

# Q3: Preorder Traversal
def preorder(node):

    if node:
        print(node.data, end=" ")

        preorder(node.left)
        preorder(node.right)

print("Preorder Traversal:")
preorder(root)

print("\n---------------------------")

# Q4: Inorder Traversal
def inorder(node):

    if node:
        inorder(node.left)

        print(node.data, end=" ")

        inorder(node.right)

print("Inorder Traversal:")
inorder(root)

print("\n---------------------------")

# Q5: Postorder Traversal
def postorder(node):

    if node:
        postorder(node.left)
        postorder(node.right)

        print(node.data, end=" ")

print("Postorder Traversal:")
postorder(root)

print("\n---------------------------")

# Q6: Count total nodes
def count_nodes(node):

    if node is None:
        return 0

    return 1 + count_nodes(node.left) + count_nodes(node.right)

print("Total Nodes:", count_nodes(root))

print("---------------------------")

# Q7: Find height of tree
def height(node):

    if node is None:
        return 0

    left_height = height(node.left)
    right_height = height(node.right)

    return 1 + max(left_height, right_height)

print("Tree Height:", height(root))

print("---------------------------")

# Q8: Search element in tree
def search(node, target):

    if node is None:
        return False

    if node.data == target:
        return True

    return search(node.left, target) or search(node.right, target)

target = int(input("Enter value to search: "))

if search(root, target):
    print("Element Found")
else:
    print("Element Not Found")

print("---------------------------")

# Q9: Sum of all nodes
def sum_nodes(node):

    if node is None:
        return 0

    return node.data + sum_nodes(node.left) + sum_nodes(node.right)

print("Sum of Nodes:", sum_nodes(root))

print("---------------------------")

# Q10: Check leaf nodes
def leaf_nodes(node):

    if node:

        if node.left is None and node.right is None:
            print(node.data, end=" ")

        leaf_nodes(node.left)
        leaf_nodes(node.right)

print("Leaf Nodes:")
leaf_nodes(root)
