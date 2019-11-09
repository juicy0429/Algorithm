def solve(m, n):
    if m == n:
        return 0
​
    if dp_arr[m][n] != -1:
        return dp_arr[m][n]
    ans = dp_arr[m][n]
​
    cost = sum(files[m:n+1])
​
    for k in range(m, n):
        tmp = solve(m, k) + solve(k+1, n) + cost
        if ans == -1 or ans > tmp:
            ans = tmp
    dp_arr[m][n] = ans
    return ans
​
TC = int(input())
​
for _ in range(TC):
    K = int(input())
    files = list(map(int, input().split()))
​
    dp_arr = [ [-1] * K for _ in range(K) ]
    ans = solve(0, K-1)
    print(ans)