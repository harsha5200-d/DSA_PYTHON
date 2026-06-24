class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):

        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# helper: level order print
from collections import deque

def levelOrder(root):
    if not root:
        return []

    q = deque([root])
    res = []

    while q:
        node = q.popleft()
        res.append(node.val)

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return res


# INPUT TREE
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# INVERT
sol = Solution()
new_root = sol.invertTree(root)

# OUTPUT
print(levelOrder(new_root))