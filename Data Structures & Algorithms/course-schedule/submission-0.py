class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(numCourses)}

        for src, dest in prerequisites:
            adj_list[src].append(dest)

        # look for cycles
        visited = set()
        visiting = set()

        def dfs(node):
            if node in visiting:
                return True
            if node in visited:
                return False

            visiting.add(node)

            for n in adj_list[node]:
                if dfs(n):
                    return True
            
            visiting.remove(node)
            visited.add(node)

            return False

        for i in range(numCourses):
            if dfs(i):
                return False
        return True