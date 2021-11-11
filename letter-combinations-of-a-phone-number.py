class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        arr = [[''], [''], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        ans = []
        idx = 0
        n = len(digits)
        while idx < n:
            char = digits[idx]
            new_ans = []
            candidates = arr[int(char)]
            for c in candidates:
                if not ans:
                    new_ans.append(c)
                else:
                    for a in ans:
                        new_ans.append(a + c)
            ans = new_ans
            idx += 1
        return ans