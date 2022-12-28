[![Language](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org)
![](https://img.shields.io/github/issues/akashsonowal/coding-with-akash?style=plastic)
![](https://img.shields.io/github/forks/akashsonowal/coding-with-akash)
![](https://img.shields.io/github/stars/akashsonowal/coding-with-akash)
![](https://img.shields.io/github/license/akashsonowal/coding-with-akash)

# Data Structures & Algorithms

## 01. Arrays
| Problem Link | Platform | Level | Solution (in Python) Link |
| --- | --- | --- | --- |
| [Two Sum](https://leetcode.com/problems/two-sum/) | LeetCode | Easy | [O(n)](https://github.com/akashsonowal/coding-with-akash/blob/main/Arrays/Easy/two_sum.py) |
| [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | LeetCode | Easy | |
| [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) | LeetCode | Easy | |
| [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/) | LeetCode | Easy | |
| [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | LeetCode | Medium | |
| [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | LeetCode | Medium | |
| [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | LeetCode | Hard | |

## 02. Linked Lists


## Stacks & Queues

## Recursion
| Problem Link | Platform | Level | Solution (in Python) Link |
| --- | --- | --- | --- |
| [Kth Largest Element in an Array (Sorting)](https://leetcode.com/problems/kth-largest-element-in-an-array/) | LeetCode | Medium | | 
| [Find First and Last Position of Element in Sorted Array (Binary Search)](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | LeetCode | Medium | | 

## Hash Maps

## Trees

## Binary Search Trees

## Heaps

## Graphs

## Dynamic Programming
| Problem Link | Platform | Level | Solution (in Python) Link |
| --- | --- | --- | --- |
| [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | LeetCode | Easy | |


# Algorithms

## Recursion

```
def fib(n):
  if n == 0: #base case
    return 0
  elif n == 1 or n == 2: #base case
    return 1
  else:
    return fib(n-1) + fib (n-2)
```
reptitive calls leads to undesirable exponential runtime and memory usage. Recursive calls are stored on stack and there is limited allocated memory for a program.

## Interation

There is no overwheming of call stack.

```
def fib(n):
  if n == 0:
    return 0
  elif n == 1 or n == 2:
    return 1
  else:
    prev2 = 0 # fib(n - 2)
    prev = 1 # fib(n - 1)
    res = 0 # fib(n)
    for i in range(1, n): #process iteratively
      res = prev + prev2
      prev2 = prev
      prev = res
    return res
```
## Greedy Algorithms

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

## Greedy Algorithms vs Dynamic Programming

Greedy Algorithms always does local optimization while dynamic programming is always guaranteed to find the globally optimal solution because it exhaust the search space.

```
0/1 Knapsack problem


```

## Sorting

## Basic Problem Solving Techniques
- Time Complexity Analysis
- Arrays
- Bit Manipulation
- Maths
- Recursion & Sorting
- Binary Search & 2 Pointers
- Hashing
- Pattern Matching Algorithms

## Data Structures
- Linked Lists
- Stacks & Queues
- Trees
- Tries & Heaps

## Advanced Problem Solving Techniques
- Greedy Algorithms
- Backtracking
- Dynamic Programming
- Graphs

## Programming Language Internals
- Data Types and Syntax
- Programming Paradigms for the Language
- Collections framework/ standard library
- Concurrency
- Advanced Concepts and Common Pitfalls

## DBMS
- SQL

## Operating Systems
- Concurrency & Synchronization

## Computer Networks
- Socket Programming

