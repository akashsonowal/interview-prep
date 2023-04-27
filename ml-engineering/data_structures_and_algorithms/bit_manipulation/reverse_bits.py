# O(1) time | O(1) space

class Solution:
    def reverseBits(n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res
