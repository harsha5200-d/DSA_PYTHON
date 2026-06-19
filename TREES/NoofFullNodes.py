class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def NoofLeaf(root):

    if not root:
        return 0

    if root.left is None and root.right is None:
        return 0
    
    elif root.left is None or root.right is None:

        return NoofLeaf(root.left) + NoofLeaf(root.right)
    else:
        return 1 + NoofLeaf(root.left) + NoofLeaf(root.right)


# Create tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

# Count leaf nodes
print("Number of full leaf nodes:", NoofLeaf(root))