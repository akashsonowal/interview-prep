[![Language](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org)
![](https://img.shields.io/github/issues/akashsonowal/coding-with-akash?style=plastic)
![](https://img.shields.io/github/forks/akashsonowal/coding-with-akash)
![](https://img.shields.io/github/stars/akashsonowal/coding-with-akash)
![](https://img.shields.io/github/license/akashsonowal/coding-with-akash)

# Data Structures & Algorithms

## Arrays
| Problem Link | Platform | Level | Solution (in Python) Link |
| --- | --- | --- | --- |
| [Two Sum](https://leetcode.com/problems/two-sum/) | LeetCode | Easy | [O(n)](https://github.com/akashsonowal/coding-with-akash/blob/main/Arrays/Easy/two_sum.py) |
| [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | LeetCode | Easy | |
| [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) | LeetCode | Easy | |
| [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/) | LeetCode | Easy | |
| [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | LeetCode | Medium | |
| [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | LeetCode | Medium | |
| [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | LeetCode | Hard | |

## Linked Lists


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
  n = len(coins) #we have 4 coins of different denominations. We can use as many from each of them.
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

## Sorting


