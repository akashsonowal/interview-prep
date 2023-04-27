# O(n) time | O(1) space

class Solution:
    @staticmethod
    def canJump(nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False 
      
assert Solution.canJump([2, 3, 1, 1, 4]) == True
