n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

for x in range(n, 0, -1):
    if a[x - 1] >= x:
        print(x)
        break
else:
    print(0)
