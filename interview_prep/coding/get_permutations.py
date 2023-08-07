
def get_permutations(nums):
    permutations = []

    if len(nums) <= 1:
        return [nums] 
    else:
        for i in nums:
            prev = nums[:i]
            next_ = nums[i + 1:]
            permutations.append(get_permutations(prev) + i + get_permutations(next_))
        return permutationss

if __name__ == "__main__":
    pass
#     a = [2, 3, 4]


# (1, 2, 3, 4)

# 2 -> (2, 3, 4) -> (2, 4, 3)
# 3 -> (4, 3, 2)
# 4 -> (3, 2, 4)
# (4, 2, 3)
# (3, 4, 2)