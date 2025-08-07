# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

    def invertTree(self, root):
        if not root: return root

        self.invertTree(root.left)
        self.invertTree(root.right)

        root_left = root.left
        root_right = root.right
        root.left = root_right
        root.right = root_left

        return root

    def isSymmetric(self, root):
        left = root.left
        right = root.right
        inv_left = self.invertTree(left)
        return self.isSameTree(right, inv_left)



root = TreeNode(1)
root.left = TreeNode(2, left=TreeNode(3), right=TreeNode(4))
root.right = TreeNode(2, left=TreeNode(4), right=TreeNode(3))

print(Solution().isSymmetric(root))