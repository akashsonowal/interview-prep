class Solution:
    @staticmethod
    def checkValidString_greedy(s: str) -> bool: #o(N) time | O(1) space
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1 #")", "("
            
            if leftMax < 0:
                return False
            if leftMin  < 0:
                leftMin = 0
        return leftMin == 0
      
      
    @staticmethod
    def checkValidString_dp(self, s: str) -> bool: #O(n2) time | O(n2) space
        dp = {(len(s), 0): True} #key=(i, leftCount) -> isValid

        def dfs(i, left):
            if i == len(s) or left < 0:
                return left == 0
            if (i, left) in dp:
                return dp[(i, left)]
            if s[i] == "(":
                dp[(i, left)] = dfs(i + 1, left + 1)
            elif s[i] == ")":
                dp[(i, left)] = dfs(i + 1, left - 1)
            else:
                dp[(i, left)] = (dfs(i + 1, left + 1) or dfs(i + 1, left - 1) or dfs(i + 1, left))
            return dp[(i, left)] 
        return dfs(0, 0)  
