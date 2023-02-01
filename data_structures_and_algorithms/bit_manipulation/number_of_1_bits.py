class Solution:
  
    @staticmethod
    def hammingWeight_bit_shift(n: int) -> int:
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res
      
    @staticmethod
    def hammingWeight_and_op(self, n: int) -> int:
        res = 0
        while n:
            n &= (n - 1)
            res += 1
        return res
