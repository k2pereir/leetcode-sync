class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if char in p.keys():
                stack.append(char)
            elif char in p.values():
                if not stack or p[stack[-1]] != char:
                    return False
                stack.pop()
        
        return len(stack) == 0
