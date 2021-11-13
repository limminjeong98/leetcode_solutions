# time limit not solved => two pointer
class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        flag = False
        for i in range(n // 2 + 1):
            if s[i] != s[n - 1 - i]:
                flag = True
                break
        if not flag:
            return True
        
        for i in range(n):
            flag = False
            new_s = s[:i] + s[i + 1:]
            new_n = len(new_s)
            new_s = str(new_s)
            for j in range(new_n // 2 + 1):
                if new_s[j] != new_s[new_n - 1 - j]:
                    flag = True
                    break
            if not flag:
                return True
        return False
                    
                    
            
        