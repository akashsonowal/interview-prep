# O(n + m) time for set creation | O(n + m) space

class Solution:
    @staticmethod
    def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
        set_1 = set(nums1)
        set_2 = set(nums2)

        if len(set_1) < len(set_2):
            return [x for x in set_1 if x in set_2]
        else:
            return [x for x in set_2 if x in set_1]

A = [1, 2, 3, 4, 5]
B = [0, 1, 3, 7]
assert Solution.intersection(A, B) == [1,  3]
