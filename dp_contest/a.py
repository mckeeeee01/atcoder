n = int(input())
h = list(map(int, input().split()))
dp = [0] * (n + 2)
for i in range(1, n):
    if i - 2 >= 1:
        dp[i] = min(dp[i - 1] + abs(h[i - 1] - h[i - 2]), dp[i - 2] + abs(h[i - 2] - h[i]))
    else:
        dp[i] = dp[i - 1] + abs(h[i-1] - h[i])
    

print(dp[n-1])