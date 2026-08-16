class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []

        for op in operations:
            if op == '+':
                ans.append(int(ans[-1]) + int(ans[-2]))
            elif op == 'C':
                ans.pop()
            elif op == 'D':
                ans.append(ans[-1] * 2)
            else:
                try:
                    ans.append(int(op))
                except:
                    continue

        return sum(ans)
        
