class Solution:
    def isValid(self, s: str) -> bool:
        closes = {
            ")": "(", 
            "}": "{", 
            "]": "["
            }
        stack = []

        for i in s:
            if i in closes:
                if stack and stack[-1] == closes[i]:
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(i)

        if not stack:
            return True
        else: 
            return False