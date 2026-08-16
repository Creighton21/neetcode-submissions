# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        value = None
        i = 0
        def dfs(node):
            nonlocal value
            nonlocal i
            if not node or value is not None:
                return

            dfs(node.left)
            i += 1
            if i == k:
                value = node.val
                return
            dfs(node.right)

        dfs(root)

        return value