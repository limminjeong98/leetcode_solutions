from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for candidates in list(permutations(nums, n)):
            if candidates in ans:
                continue
            ans.append(candidates)
        return ans