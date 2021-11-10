class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        n = len(strs)
        i = 0
        flag = False
        min_len = int(1e9)
        while True:
            if len(strs[0]) <= i:
                break
            cur = strs[0][i]
            for j in range(1, n):
                if len(strs[j]) <= i:
                    flag = True
                    break
                if cur != strs[j][i]:
                    flag = True
                    break
            if flag:
                break
            i += 1
            ans += cur
        return ans