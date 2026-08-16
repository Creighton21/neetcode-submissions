class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '[' or c == '{' or c == '(':
                stack.append(c)
                continue
            try:
                top = stack.pop()
            except:
                return False

            if (c != ']' and top == '[') or (c != '}' and top == '{') or (c != ')' and top == '('):
                return False
            
        if len(stack) == 0:
            return True
        else:
            return False