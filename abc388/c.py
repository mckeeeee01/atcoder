n = int(input())
a = list(map(int, input().split()))


ans = 0
j = 0

for i in a:
    while j < n and a[j] * 2 <= i:
        j += 1
    ans += j

print(ans)
