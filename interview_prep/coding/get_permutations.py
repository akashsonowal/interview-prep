
def get_permutations(nums):
    if len(nums) <= 1:
        return [nums] 
    else:
        for i in range(nums):
            pass


if __name__ == "__main__":
    a = [2, 3, 4]


(1, 2, 3, 4)

2 -> (2, 3, 4) -> (2, 4, 3)
3 -> (4, 3, 2)
4 -> (3, 2, 4)
(4, 2, 3)
(3, 4, 2)