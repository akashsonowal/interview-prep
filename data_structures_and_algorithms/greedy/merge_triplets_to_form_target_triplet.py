# O(n) time | O(1) space

class Solution:
    @staticmethod
    def mergeTriplets(triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
                    
        return len(good) == 3

triplets = [[2,5,3],[1,8,4],[1,7,5]]
target = [2,7,5]
assert Solution.mergeTriplets(triplets, target) == True
