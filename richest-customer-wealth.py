class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m, n = len(accounts), len(accounts[0])
        ans = 0
        for i in range(m):
            if ans < sum(accounts[i]):
                ans = sum(accounts[i])
        return ans