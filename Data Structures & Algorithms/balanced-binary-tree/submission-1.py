class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def postorder(root):
            nonlocal balanced
            if not root:
                return 0
            
            h1 = postorder(root.left)
            h2 = postorder(root.right)

            if abs(h1 - h2) > 1:
                balanced = False

            return max(h1, h2) + 1

        postorder(root)
        return balanced