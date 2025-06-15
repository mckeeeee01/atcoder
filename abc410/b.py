n,q = map(int, input().split())
x = list(map(int, input().split()))

ans = []
box = [0] * n
for i in range(q):
    if x[i] == 0:
        tmp = min(box)
        for j in range(n):
            if box[j] == tmp:
                box[j] += 1
                ans.append(j+1)
                break
    else:
        ans.append(x[i])
        box[x[i]-1] += 1
        
print(*ans)
