# Greedy Algorithms

At each step choose best option.

Making change with the minimum number of coins

```
def minCoins(k):
  coins = [1, 5, 10, 25] #pennies, nickles, dimes, quarters
  n = len(coins) #we have 4 different denominations of coins. We can use as many from each of them.
  res = []
  i = n - 1 #start at last index
  while(i >= 0  and k >= 0):
    if k >= coins[i]:
      k -= coins[i]
      res.append(coins[i])
    else:
      i -= 1
  return res
```

In ML, decision trees are split in a greedy manner to maximise information gain (reduction in entropy based on feature chosen) at each split. For every feature, we evaluate all features, then in a greedy fashion, choose the feature with the best information gain to split on next. This repeats until we end up with leaf nodes.
```
info_gains = [getInfoGains(feature) for feature in features]
best_feature_index = np.argmax(info_gains)
best_feature = features[best_feature_index]
```
For optimization problem, use greedy when there's an obvious set of choices to select from and it's easy to know what the appropriate choice is.

Note: It is easy to reason about a greedy algorithm recursively, but then implement it later iteratively for better memory performance.

## Greedy Algorithms vs Dynamic Programming

Greedy Algorithms always does local optimization while dynamic programming is always guaranteed to find the globally optimal solution because it exhaust the search space.

```
0/1 Knapsack problem
```

| Problem Link | Platform | Level | Solution (in Python) Link |
| --- | --- | --- | --- |
| [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | LeetCode | Medium
| [Jump Game](https://leetcode.com/problems/jump-game/) | LeetCode | Medium
| [Jump Game 2](https://leetcode.com/problems/jump-game-ii/) | LeetCode | Medium
| [Gas Station](https://leetcode.com/problems/gas-station/) | LeetCode | Medium
| [Hand of Straights](https://leetcode.com/problems/hand-of-straights/) | LeetCode | Medium
| [Merge Triplets to Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) | LeetCode | Medium
| [Partition Labels](https://leetcode.com/problems/partition-labels/) | LeetCode | Medium
| [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) | LeetCode | Medium



