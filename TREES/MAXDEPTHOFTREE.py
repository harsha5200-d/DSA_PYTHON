# Definition of TreeNode
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Recursive function to construct the tree
def buildTree():
    data = input("Enter node value (-1 for NULL): ")

    if data == "-1":
        return None

    root = TreeNode(int(data))

    print(f"Enter left child of {data}")
    root.left = buildTree()

    print(f"Enter right child of {data}")
    root.right = buildTree()

    return root


# Function to find maximum depth
def maxDepth(root):
    if not root:
        return 0

    return max(1 + maxDepth(root.left),
               1 + maxDepth(root.right))


# Driver Code
print("Construct Binary Tree:")
root = buildTree()

print("\nMaximum Depth of Tree:", maxDepth(root))