def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    seen = {}
    for idx, value in enumerate(nums):
        compl = target - value

        if compl in seen:
            return [seen[compl], idx]

        seen[value] = idx
    return []


assert two_sum([2, 3, 5, 1], 6) == [2, 3]
assert two_sum([2, 3, 5, 1], 8) == [1, 2]
assert two_sum([2, 3, 5, 1], 10) == []
assert two_sum([2, 3, 3, 1], 6) == [1, 2]
