# O(n) time | O(n * m) space where n is the len of list and m is the sum of the elements in n

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # (index, total)

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i])
            return dp[(i, total)]
        
        return backtrack(0, 0)
