# Day 44: Binary Tree Interview Problems

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Q1: Create Binary Tree
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)

print("Binary Tree Created")

print("---------------------------")

# Q2: Inorder Traversal
def inorder(node):

    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

print("Inorder Traversal:")
inorder(root)

print("\n---------------------------")

# Q3: Preorder Traversal
def preorder(node):

    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

print("Preorder Traversal:")
preorder(root)

print("\n---------------------------")

# Q4: Postorder Traversal
def postorder(node):

    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")

print("Postorder Traversal:")
postorder(root)

print("\n---------------------------")

# Q5: Count Total Nodes
def count_nodes(node):

    if node is None:
        return 0

    return 1 + count_nodes(node.left) + count_nodes(node.right)

print("Total Nodes:", count_nodes(root))

print("---------------------------")

# Q6: Find Height of Tree
def height(node):

    if node is None:
        return 0

    left_height = height(node.left)
    right_height = height(node.right)

    return 1 + max(left_height, right_height)

print("Height:", height(root))

print("---------------------------")

# Q7: Search in Tree
def search(node, target):

    if node is None:
        return False

    if node.data == target:
        return True

    return search(node.left, target) or search(node.right, target)

target = int(input("Enter value to search: "))

if search(root, target):
    print("Value Found")
else:
    print("Value Not Found")

print("---------------------------")

# Q8: Sum of All Nodes
def sum_nodes(node):

    if node is None:
        return 0

    return node.data + sum_nodes(node.left) + sum_nodes(node.right)

print("Sum of Nodes:", sum_nodes(root))

print("---------------------------")

# Q9: Count Leaf Nodes
def count_leaf_nodes(node):

    if node is None:
        return 0

    if node.left is None and node.right is None:
        return 1

    return (
        count_leaf_nodes(node.left)
        + count_leaf_nodes(node.right)
    )

print("Leaf Nodes Count:", count_leaf_nodes(root))

print("---------------------------")

# Q10: Print Leaf Nodes
def print_leaf_nodes(node):

    if node:

        if node.left is None and node.right is None:
            print(node.data, end=" ")

        print_leaf_nodes(node.left)
        print_leaf_nodes(node.right)

print("Leaf Nodes:")
print_leaf_nodes(root)
