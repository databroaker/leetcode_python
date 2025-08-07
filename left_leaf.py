class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sumOfLeftLeaves(self, root):
        total = 0

        if root:
            left = root.left
            right = root.right
            if left and not left.left and not left.right:
                total += left.val
            else:
                total += self.sumOfLeftLeaves(left)
            if right:
                total += self.sumOfLeftLeaves(right)

        return total

# [3,9,20,null,null,15,7]

tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(Solution().sumOfLeftLeaves(tree))