n = int(input())
d = list(map(int, input().split()))


for i in range(n-1):
    tmp = 0
    for j in range(i, n-1):
        tmp += d[j]
        print(tmp, end=" ")
    print("")