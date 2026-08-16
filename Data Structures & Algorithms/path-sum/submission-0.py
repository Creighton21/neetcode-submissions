# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def search(root, path):
            if not root:
                return False

            path.append(root.val)

            # At a leaf
            if not root.left and not root.right:
                if sum(path) == targetSum:
                    return True
            
            if search(root.left, path):
                return True
            if search(root.right, path):
                return True

            path.pop()
            return False
        path = []
        return search(root, path)