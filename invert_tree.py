class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        if not root: return root

        self.invertTree(root.left)
        self.invertTree(root.right)

        root_left = root.left
        root_right = root.right
        root.left = root_right
        root.right = root_left

        return root

tree = TreeNode(4)
tree.left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
tree.right = TreeNode(7, left=TreeNode(6), right=TreeNode(9))
done = Solution().invertTree(tree)
print(done)