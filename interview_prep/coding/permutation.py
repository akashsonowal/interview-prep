def permute(nums):
    res = []
    n = len(nums)
    if n <= 1:
        return [nums]
    else:
        for i in range(len(nums)):
            for combo in permute(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + combo)
    return res

if __name__ == "__main__":
    assert permute([2, 3, 4]) == [[2, 3, 4], [2, 4, 3], [3, 2, 4], [3, 4, 2], [4, 2, 3], [4, 3, 2]]