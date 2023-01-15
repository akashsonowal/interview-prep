# O(m * n) time | O(m * n) space

class Solution:
  
    @staticmethod
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {} # (r, c)

        def dfs(r, c, prevValue):
            if r < 0 or r == len(matrix) or c < 0 or c == len(matrix[0]) or matrix[r][c] <= prevValue:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))

            dp[(r, c)] = res 

            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        
        return max(dp.values())

matrix = [[9,9,4],[6,6,8],[2,1,1]]

assert Solution.longestIncreasingPath(matrix) == 4
