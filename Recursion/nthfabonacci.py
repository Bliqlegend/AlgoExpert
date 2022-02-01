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
def LMgetNthFib(n):
    dp = [-1 for i in range(n)]
    if n == 1:
        return 0
    if n == 2:
        if dp[n-1] == -1:
            op = LMgetNthFib(n-1)
            dp[n-1] = op
            return 1 + op
        else:
            return 1 + dp[n-1]
    if dp[n-1] == -1 and dp[n-2] == -1:
        op2 = LMgetNthFib(n-2)
        op1 = LMgetNthFib(n-1)
        dp[n-2],dp[n-1] = op2,op1
        return op2 + op1
    elif dp[n-1] == -1 and dp[n-2] != -1:
        op2 = dp[n-2]
        op1 = LMgetNthFib(n-1)
        dp[n-1] = op1
        return op2 + op1
    elif dp[n-2] == -1 and dp[n-1] != -1:
        op2 = LMgetNthFib(n-2)
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

def getNthFib(n):
    dp = {1:0,2:1}
    for i in range(3,n+1):
        if i -2 < 0:
            break
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n] 

def fbLast(n):
    lastTwo = [0,1]
    c = 3
    while c <= n:
        nn = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nn
        c+=1
    return lastTwo[1] if n > 1 else lastTwo[0]
 
n = int(input())   
# dp = [-1 for i in range(n)]
# ans = getNthFib(n)
# ans = getNthFibShortMemoization(n)
ans = fbLast(n)
print(ans)
