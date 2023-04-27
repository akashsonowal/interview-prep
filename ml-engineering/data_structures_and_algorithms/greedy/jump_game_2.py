# O(n) time | O(1) space

class Solution:
    @staticmethod
    def jump(nums: List[int]) -> int:
        res = 0
        l = r = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res

assert Solution.jump([2,3,1,1,4]) == 2
