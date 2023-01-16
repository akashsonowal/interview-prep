# O(n * m) time | O(n * m) space

class Solution:
    @staticmethod
    def numDistinct(s: str, t: str) -> int:
        cache = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            
            if s[i] == t[j]:
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                cache[(i, j)] = dfs(i + 1, j)
            return cache[(i, j)]
        
        return dfs(0, 0)
      
s = "rabbbit", t = "rabbit"
assert Solution.numDistinct(s, t) == 3
 
