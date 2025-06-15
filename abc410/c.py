n,q = map(int, input().split())

a = [i + 1 for i in range(n)]

query = []
for i in range(q):
    query.append(list(map(int, input().split())))


offset = 0

for i in range(q):
    tmp = query[i][0]
    if tmp == 1:
        idx = (query[i][1] - 1 + offset) % n
        a[idx] = query[i][2]
    elif tmp == 2:
        idx = (query[i][1] - 1 + offset) % n
        print(a[idx])
    else: #tmp == 3
        shift = query[i][1] % n
        offset = (offset + shift) % n

