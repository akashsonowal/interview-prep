from collections import queue

def longest_wellformed_string(x):
    res = 0
    for i in range(len(x) // 2):
        if x[i] == x[len(x) - i - 1]:
            res += 1
    return res

if __name__ == "__main__":
    assert longest_wellformed_string(")(())(") == 4