class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def postorder(root):
            nonlocal balanced
            if not root:
                return 0
            
            h1 = postorder(root.left)
            h3 = h1 + 1
            h2 = postorder(root.right)
            h4 = h2 + 1

            if abs(h3 - h4) > 1:
                balanced = False

            return max(h3, h4)

        postorder(root)
        return balanced