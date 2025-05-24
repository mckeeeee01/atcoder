h, w, n = map(int, input().split())
row_stones = [set() for _ in range(h)]
col_stones = [set() for _ in range(w)]

for i in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    row_stones[x].add(y)
    col_stones[y].add(x)

q = int(input())

for i in range(q):
    query, num = map(int, input().split())
    num -= 1
    if query == 1:
        count = len(row_stones[num])
        for y in row_stones[num]:
            col_stones[y].remove(num)
        row_stones[num].clear()
    else:
        count = len(col_stones[num])
        for x in col_stones[num]:
            row_stones[x].remove(num)
        col_stones[num].clear()
    print(count)
