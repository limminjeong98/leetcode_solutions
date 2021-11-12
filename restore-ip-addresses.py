class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        if n < 4 or n > 12:
            return ans
        for i in range(3):
            if i != 0 and s[0] == '0':
                continue
            first = s[:i + 1]
            if int(first) > 255:
                continue
            for j in range(i + 1, i + 4):
                if j > n:
                    continue
                if j != i + 1 and s[i + 1] == '0':
                    continue
                second = s[i + 1:j + 1]
                if int(second) > 255:
                    continue
                for k in range(j + 1, j + 4):
                    if k + 1 >= n:
                        continue
                    if k != j + 1 and s[j + 1] == '0':
                        continue
                    third = s[j + 1:k + 1]
                    if int(third) > 255:
                        continue
                    last = s[k + 1:]
                    if not last or len(last) > 3:
                        continue
                    if len(last) >= 2 and s[k + 1] == '0':
                        continue
                    if int(last) > 255:
                        continue
                    arr = [first, second, third, last]
                    ans.append('.'.join(arr))
        return ans
        