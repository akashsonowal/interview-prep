## Dynamic Programming

Dynamic Programming speeds up recursion (storing results of subproblems)

```
dp = [0] * 1000

def fib(n):
  if n == o or n == 1:
    return n
  else:
    dp[n] = fib(n-1) + fib(n-2)
    return dp[n]
```
For DP two properties needs to be satisfied:
1. Optimal substructure (i.e., problem can be broken down)
2. Overlapping subproblems (i.e., reusable in other subproblems)

Solved using:
1. Top-Down: start from final (recursion)
2. Bottom-Up: start from simplest use case (iterative)

```
Bottom up Approach

def fib(n):
  dp = [0 for _ in range(n+1)]
  dp[1] = 1
  for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
   return dp[n]
```
Example of dynamic programming is reinforcement learning (Bellman equation).

## 1-D Dynamic Programming

| Problem Link | Platform | Level | Solution (in Python) Link |
| --- | --- | --- | --- |
| [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | LeetCode | Easy
| [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | LeetCode | Easy
| [House Robber](https://leetcode.com/problems/house-robber/) | LeetCode | Medium
| [House Robber 2](https://leetcode.com/problems/house-robber-ii/) | LeetCode | Medium
| [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | LeetCode | Medium
| [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | LeetCode | Medium
| [Decode Ways](https://leetcode.com/problems/decode-ways/) | LeetCode | Medium
| [Coin Change](https://leetcode.com/problems/coin-change/) | LeetCode | Medium
| [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | LeetCode | Medium
| [Word Break](https://leetcode.com/problems/word-break/) | LeetCode | Medium
| [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | LeetCode | Medium
| [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | LeetCode | Medium

## 2-D Dynamic Programming

| Problem Link | Platform | Level | Solution (in Python) Link |
| --- | --- | --- | --- |
| [Unique Paths](https://leetcode.com/problems/unique-paths/) | LeetCode | Medium
| [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | LeetCode | Medium
| [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | LeetCode | Medium
| [Coin Change II](https://leetcode.com/problems/coin-change-ii/) | LeetCode | Medium
| [Target Sum](https://leetcode.com/problems/target-sum/) | LeetCode | Medium
| [Interleaving String](https://leetcode.com/problems/interleaving-string/) | LeetCode | Medium
| [Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | LeetCode | Hard
| [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) | LeetCode | Hard
| [Edit Distance](https://leetcode.com/problems/edit-distance/) | LeetCode | Hard
| [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | LeetCode | Hard






