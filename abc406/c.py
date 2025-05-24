n = int(input())
a = list(map(int, input().split()))

diff = [0] * (n - 1)
for i in range(n - 1):
    if a[i] < a[i + 1]:
        diff[i] = 0
    else:
        diff[i] = 1


rle = []
for x in diff:
    if rle and rle[-1][0] == x:
        rle[-1] = (rle[-1][0], rle[-1][1] + 1)
    else:
        rle.append((x, 1))

ans = 0
for i in range(len(rle)):
    if rle[i][0] == 1:
        l, r = 0, 0
        if 0 < i:
            l = rle[i - 1][1]
        if i + 1 < len(rle):
            r = rle[i + 1][1]
        ans += l * r

print(ans)

