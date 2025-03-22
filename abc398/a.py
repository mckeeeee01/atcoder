n = int(input())

ans = ""
if n % 2 == 0:
    for i in range(1,n + 1):
        if i == n // 2 or i == n // 2 + 1:
            ans += "="
        else:
            ans += "-"
            
else:
    for i in range(n):
        if i == n // 2:
            ans += "="
        else:
            ans += "-"

print(ans)