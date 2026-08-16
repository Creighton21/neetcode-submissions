# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []

        """
        BFS
        return right most node at all given levels
        """

        queue = deque()

        queue.append(root)

        while len(queue) > 0:
            n = len(queue)
            level = []
            for i in range(n):
                curr = queue.popleft()
                if curr:
                    level.append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)

            if level:
                result.append(level[-1])


        return result