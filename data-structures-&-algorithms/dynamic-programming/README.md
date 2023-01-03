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

## 2-D Dynamic Programming

| Problem Link | Platform | Level | Solution (in Python) Link |
| --- | --- | --- | --- |
