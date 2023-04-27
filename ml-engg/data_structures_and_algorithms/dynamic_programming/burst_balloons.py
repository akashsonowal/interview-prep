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
    
    @staticmethod
    def maxCoins_iterative(nums: List[int]) -> int:
        cache = {}
        nums = [1] + nums + [1]

        for offset in range(2, len(nums)):
            for left in range(len(nums) - offset):
                right = left + offset
                for pivot in range(left + 1, right):
                    coins = nums[left] * nums[pivot] * nums[right]
                    coins += cache.get((left, pivot), 0) + cache.get((pivot, right), 0)
                    cache[(left, right)] = max(coins, cache.get((left, right), 0))
        return cache.get((0, len(nums) - 1), 0)
