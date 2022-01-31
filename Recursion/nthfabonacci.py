# Nth Fabonacci

# FC1 : Brute force 
# getNthFib : Memoization or caching (array based)
# getNthFibShortMemoization : Memoization or caching (hashmap based)

import sys
sys.setrecursionlimit(10**6)

# brute force approach
# O(2^n) time
def fc1(n):
    if n == 1:
        return 0
    if n == 2:
        return 1 + fc1(n-1)
    return fc1(n-2) + fc1(n-1)

# array based memoization
# O(N) time
def getNthFib(n):
    dp = [-1 for i in range(n)]
    if n == 1:
        return 0
    if n == 2:
        if dp[n-1] == -1:
            op = getNthFib(n-1)
            dp[n-1] = op
            return 1 + op
        else:
            return 1 + dp[n-1]
    if dp[n-1] == -1 and dp[n-2] == -1:
        op2 = getNthFib(n-2)
        op1 = getNthFib(n-1)
        dp[n-2],dp[n-1] = op2,op1
        return op2 + op1
    elif dp[n-1] == -1 and dp[n-2] != -1:
        op2 = dp[n-2]
        op1 = getNthFib(n-1)
        dp[n-1] = op1
        return op2 + op1
    elif dp[n-2] == -1 and dp[n-1] != -1:
        op2 = getNthFib(n-2)
        op1 = dp[n-1]
        dp[n-2] = op2
        return op2 + op1
    else:
        op2 = dp[n-2]
        op1 = dp[n-1]
        return op1 + op2

# hashmap memoization (44steps ; n=6)
# O(N) time
def getNthFibShortMemoization(n,dp={1:0,2:1}):
    if n in dp:
        return dp[n]
    else:
        dp[n] = getNthFibShortMemoization(n-1,dp) + getNthFibShortMemoization(n-2,dp)
        return dp[n]

n = int(input())
# ans = fc1(n)
# dp = [-1 for i in range(n)]
# ans = getNthFib(n)
ans = getNthFibShortMemoization(n)
print(ans)
