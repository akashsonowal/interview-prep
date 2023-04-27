# O(n) time | O(1) space

class Solution:
    @staticmethod
    def partitionLabels(s: str) -> List[int]:
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i
        
        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])
            if i == end:
                res.append(size)
                size = 0
        return res

s = "ababcbacadefegdehijhklij"
assert Solution.partitionLabels(s) == [9,7,8]
