class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def dfs(root):
            nonlocal balanced
            if not root:
                return 0
            
            h1 = dfs(root.left)
            h2 = dfs(root.right)

            if abs(h1 - h2) > 1:
                balanced = False

            return max(h1, h2) + 1

        dfs(root)
        return balanced