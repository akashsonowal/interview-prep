[![Language](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org)
![](https://img.shields.io/github/issues/akashsonowal/coding-with-akash?style=plastic)
![](https://img.shields.io/github/forks/akashsonowal/coding-with-akash)
![](https://img.shields.io/github/stars/akashsonowal/coding-with-akash)
![](https://img.shields.io/github/license/akashsonowal/coding-with-akash)

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


# Extra Notes

Data Structures and Algorithms
Research Papers Implementations
SQL
ML Coding

PyTorch
Tensorflow
JAX
PyTorch in production:

Convert PyTorch to TorchScript models that can be run in C++ apps. Two methods to convert torch models to torchscript models: annotation and trace.
