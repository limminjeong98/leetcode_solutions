from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for candidates in list(permutations(nums, n)):
            ans.append(candidates)
        return ans
        