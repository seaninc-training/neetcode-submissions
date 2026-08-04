class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}
        stack = []
        
        if len(s) % 2 != 0:
            return False
        
        for c in s:
            if c in pairs:
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        
        return not stack