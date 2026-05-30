# Day 38: Binary Search Tree (BST)

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# BST class
class BST:

    def __init__(self):
        self.root = None

    # Q1: Insert node
    def insert(self, root, data):

        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        return root

    # Q2: Inorder Traversal
    def inorder(self, root):

        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Q3: Preorder Traversal
    def preorder(self, root):

        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Q4: Postorder Traversal
    def postorder(self, root):

        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    # Q5: Search value
    def search(self, root, key):

        if root is None:
            return False

        if root.data == key:
            return True

        if key < root.data:
            return self.search(root.left, key)

        return self.search(root.right, key)

    # Q6: Find minimum value
    def find_min(self, root):

        while root.left:
            root = root.left

        return root.data

    # Q7: Find maximum value
    def find_max(self, root):

        while root.right:
            root = root.right

        return root.data

    # Q8: Count nodes
    def count_nodes(self, root):

        if root is None:
            return 0

        return (
            1
            + self.count_nodes(root.left)
            + self.count_nodes(root.right)
        )

    # Q9: Height of BST
    def height(self, root):

        if root is None:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)

        return 1 + max(left, right)

    # Q10: Sum of all nodes
    def sum_nodes(self, root):

        if root is None:
            return 0

        return (
            root.data
            + self.sum_nodes(root.left)
            + self.sum_nodes(root.right)
        )


# Create BST
bst = BST()

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    bst.root = bst.insert(bst.root, value)

print("Inorder Traversal:")
bst.inorder(bst.root)

print("\n---------------------------")

print("Preorder Traversal:")
bst.preorder(bst.root)

print("\n---------------------------")

print("Postorder Traversal:")
bst.postorder(bst.root)

print("\n---------------------------")

key = int(input("Enter value to search: "))

if bst.search(bst.root, key):
    print("Value Found")
else:
    print("Value Not Found")

print("---------------------------")

print("Minimum Value:", bst.find_min(bst.root))

print("---------------------------")

print("Maximum Value:", bst.find_max(bst.root))

print("---------------------------")

print("Total Nodes:", bst.count_nodes(bst.root))

print("---------------------------")

print("Height:", bst.height(bst.root))

print("---------------------------")

print("Sum of Nodes:", bst.sum_nodes(bst.root))
