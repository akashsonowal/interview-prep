def combo(n, k):
    def backtrack(n, k, res, combo, nums, start):
        if nums == k:
            res.append(list(combo))
        if start > n or nums > k:
            return
        
        for i in range(start, n + 1):
            combo.append(i)
            backtrack(n, k, res, combo, nums + 1, i + 1)
            combo.remove(i)
    res = []
    backtrack(n, k, res, [], 0, 1)
    return res  

if __name__ == "__main__":
    assert combo(3, 2) == [[1, 2], [1, 3], [2, 3]]