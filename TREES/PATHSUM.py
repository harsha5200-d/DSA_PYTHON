class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def buildTree():
    val = int(input("Enter node value (-1 for NULL): "))

    if val == -1:
        return None

    root = TreeNode(val)

    print(f"Enter left child of {val}")
    root.left = buildTree()

    print(f"Enter right child of {val}")
    root.right = buildTree()

    return root


def hasPathSum(root, targetSum):

    def helper(root, tillsum, targetSum):
        if not root:
            return False

        # Leaf node check
        if tillsum + root.val == targetSum and not root.left and not root.right:
            return True

        tillsum += root.val

        return (helper(root.left, tillsum, targetSum) or
                helper(root.right, tillsum, targetSum))

    return helper(root, 0, targetSum)


# Driver Code
print("Construct Binary Tree")
root = buildTree()

targetSum = int(input("Enter Target Sum: "))

if hasPathSum(root, targetSum):
    print("Path Exists")
else:
    print("Path Does Not Exist")