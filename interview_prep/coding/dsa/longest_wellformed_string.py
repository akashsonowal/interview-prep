def longest_parens(s):
    stack = []
    longest = 0

    n = len(s)
    stack.append(-1)

    for i in range(n):
        if s[i] == "(":
            stack.append(i)
        else:
            stack_out = stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                longest = max(longest, i - stack_out)
    return longest 

if __name__ == "__main__":
    assert longest_parens(")(())(") == 4