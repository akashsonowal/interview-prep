# O(n3) time | O(n2) space

class Solution:
    @staticmethod
    def maxCoins_recursive(nums: List[int]) -> int:
        cache = {}
        nums = [1] + nums + [1]

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in cache:
                return cache[(l, r)]

            cache[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                cache[(l, r)] = max(cache[(l, r)], coins)
            return cache[(l, r)]

        return dfs(1, len(nums) - 2)
