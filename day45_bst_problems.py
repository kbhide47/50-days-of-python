# Day 45: Binary Search Tree Problems

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# BST Class
class BST:

    def insert(self, root, data):

        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        return root

    # Q1: Inorder Traversal
    def inorder(self, root):

        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Q2: Search in BST
    def search(self, root, key):

        if root is None:
            return False

        if root.data == key:
            return True

        if key < root.data:
            return self.search(root.left, key)

        return self.search(root.right, key)

    # Q3: Find Minimum
    def find_min(self, root):

        while root.left:
            root = root.left

        return root.data

    # Q4: Find Maximum
    def find_max(self, root):

        while root.right:
            root = root.right

        return root.data

    # Q5: Count Nodes
    def count_nodes(self, root):

        if root is None:
            return 0

        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    # Q6: Height of BST
    def height(self, root):

        if root is None:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))

    # Q7: Validate BST
    def is_bst(self, root, min_val, max_val):

        if root is None:
            return True

        if not (min_val < root.data < max_val):
            return False

        return (
            self.is_bst(root.left, min_val, root.data) and
            self.is_bst(root.right, root.data, max_val)
        )

    # Q8: Sum of Nodes
    def sum_nodes(self, root):

        if root is None:
            return 0

        return root.data + self.sum_nodes(root.left) + self.sum_nodes(root.right)

    # Q9: Print range elements
    def print_range(self, root, low, high):

        if root is None:
            return

        if low < root.data:
            self.print_range(root.left, low, high)

        if low <= root.data <= high:
            print(root.data, end=" ")

        if root.data < high:
            self.print_range(root.right, low, high)

    # Q10: Find closest value
    def closest_value(self, root, target):

        closest = root.data

        while root:

            if abs(root.data - target) < abs(closest - target):
                closest = root.data

            if target < root.data:
                root = root.left
            elif target > root.data:
                root = root.right
            else:
                break

        return closest


# ---------------------------
# Create BST
bst = BST()

root = None

values = [50, 30, 70, 20, 40, 60, 80]

for v in values:
    root = bst.insert(root, v)

print("Inorder Traversal:")
bst.inorder(root)

print("\n---------------------------")

key = int(input("Enter value to search: "))

print("Found:", bst.search(root, key))

print("---------------------------")

print("Min Value:", bst.find_min(root))
print("Max Value:", bst.find_max(root))

print("---------------------------")

print("Total Nodes:", bst.count_nodes(root))

print("---------------------------")

print("Height:", bst.height(root))

print("---------------------------")

print("Is BST:", bst.is_bst(root, float("-inf"), float("inf")))

print("---------------------------")

print("Sum of Nodes:", bst.sum_nodes(root))

print("---------------------------")

low = int(input("Enter low range: "))
high = int(input("Enter high range: "))

print("Range Elements:")
bst.print_range(root, low, high)

print("\n---------------------------")

target = int(input("Enter target: "))

print("Closest Value:", bst.closest_value(root, target))
