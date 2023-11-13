class Solution:
    """
    # Brute force Solution
    # Time: O(2^m), Space: O(m)
    # Where m is the capacity.
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        return self.dfsHelper(0, profit, weight, capacity)

    def dfsHelper(self, i, profit, weight, capacity):
        if i == len(profit):
            return 0

        # Skip item i
        maxProfit = self.dfsHelper(i + 1, profit, weight, capacity)

        # Include item i
        newCap = capacity - weight[i]
        if newCap >= 0:
            p = profit[i] + self.dfsHelper(i, profit, weight, newCap)
            # Compute the max
            maxProfit = max(maxProfit, p)

        return maxProfit


    # Memoization Solution
    # Time: O(n * m), Space: O(n * m)
    # Where n is the number of items & m is the capacity.
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # A 2d array, with N rows and M + 1 columns, init with -1's
        N, M = len(profit), capacity
        cache = [[-1] * (M + 1) for _ in range(N)]
        return self.memoHelper(0, profit, weight, capacity, cache)

    def memoHelper(self, i, profit, weight, capacity, cache):
        if i == len(profit):
            return 0
        if cache[i][capacity] != -1:
            return cache[i][capacity]

        # Skip item i
        cache[i][capacity] = self.memoHelper(i + 1, profit, weight, capacity, cache)
        
        # Include item i
        newCap = capacity - weight[i]
        if newCap >= 0:
            p = profit[i] + self.memoHelper(i, profit, weight, newCap, cache)
            # Compute the max
            cache[i][capacity] = max(cache[i][capacity], p)

        return cache[i][capacity]


    # Dynamic Programming Solution
    # Time: O(n * m), Space: O(n * m)
    # Where n is the number of items & m is the capacity.
    def maximumProfit(self, profit, weight, capacity):
        N, M = len(profit), capacity
        dp = [[0] * (M + 1) for _ in range(N)]

        # Fill the first column and row to reduce edge cases
        for i in range(N):
            dp[i][0] = 0
        for c in range(M + 1):
            if weight[0] <= c:
                dp[0][c] = (c // weight[0]) * profit[0] 

        for i in range(1, N):
            for c in range(1, M + 1):
                skip = dp[i-1][c]
                include = 0
                if c - weight[i] >= 0:
                    include = profit[i] + dp[i][c - weight[i]]
                dp[i][c] = max(include, skip)
        return dp[N-1][M]
    """

    # Memory optimized Dynamic Programming Solution
    # Time: O(n * m), Space: O(m)
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        dp = [0] * (M + 1)

        for i in range(N):
            curRow = [0] * (M + 1)
            for c in range(1, M + 1):
                skip = dp[c]
                include = 0
                if c - weight[i] >= 0:
                    include = profit[i] + curRow[c - weight[i]]
                curRow[c] = max(include, skip)
            dp = curRow
        return dp[M]