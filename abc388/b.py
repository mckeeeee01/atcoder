n,d = map(int, input().split())
t = [0]*n
l = [0]*n
for i in range(n):
    t[i], l[i] = map(int, input().split())
    
tl = []*n

for i in range(1,d+1):
    tl = [0]*n
    for j in range(n):
        tl[j] = (l[j] + i) * t[j]
    print(max(tl))
