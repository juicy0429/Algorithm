MOD = 1000000007
dp_arr = [-1] * 5001
​
def solve(n):
    if n == 0:
        return 1
    if dp_arr[n] >= 0:
        return dp_arr[n]
​
    dp_arr[n] = 0
    for i in range(2, n+1, 2):
        dp_arr[n] += solve(i-2) * solve(n-i)
        dp_arr[n] %= MOD
    return dp_arr[n]
​
T = int(input())
​
for _ in range(T):
    L = int(input())
    if L % 2 == 0:
        print(solve(L))
    else:
        print(0)