class Solution:
    @staticmethod
    def missingNumber(nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])
        return res

assert Solution.missingNumber([3, 0, 1]) == 2
