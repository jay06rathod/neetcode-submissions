# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            left = max(0, left)
            right = max(0, right)

            self.res = max(self.res, curr.val+left+right)
            return curr.val + max(left, right)

        dfs(root)
        return self.res