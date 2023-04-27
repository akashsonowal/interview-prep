# O(n) time | O(1) space

class Solution:
    @staticmethod
    def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        res = 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1
        
        return res

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
assert Solution.canCompleteCircuit(gas, cost) == 3
