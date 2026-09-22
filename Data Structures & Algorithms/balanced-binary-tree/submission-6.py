# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        balanced = True

        def isBalancedN(root):
            nonlocal balanced

            if not root:
                return 0

            left_depth = isBalancedN(root.left)
            right_depth = isBalancedN(root.right)

            if abs(left_depth - right_depth) > 1:
                balanced = False

            return 1 + max(left_depth, right_depth)

        isBalancedN(root)

        return balanced