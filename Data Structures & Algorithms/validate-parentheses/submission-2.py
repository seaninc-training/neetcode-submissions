class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []

        if len(s) % 2 != 0:
            return False

        for c in s:
            if c in pairs.keys():
                if not stack or stack[-1] != pairs.get(c):
                    return False
                else: 
                    stack.pop()
            elif c in pairs.values():
                stack.append(c)
            else:
                return False
        
        if not stack: 
            return True
        else: 
            return False
                

        # if len(s) % 2 != 0:
        #     return False
        # elif s == None: 
        #     return False
        # elif s[0] in [")", "}", "]"]:
        #     return False
        # else:
        #     for i, p in enumerate(s):
        #         j = len(s) - i

        #     return True 
        