class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] == '{':
                stack.append(s[i])
            elif s[i] == '[':
                stack.append(s[i])
            elif s[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif s[i] == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif s[i] == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
                    
                