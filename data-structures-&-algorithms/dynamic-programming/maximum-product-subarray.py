#O(n) time | O(1) space

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax, currMin = 1, 1

        for n in nums:
            tmp = n*currMax
            currMax = max(n*currMax, n*currMin, n)
            currMin = min(tmp, n*currMin, n)
            res = max(res, currMax)
        return res
