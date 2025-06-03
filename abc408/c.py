n,m = map(int,input().split())

l = []
r = []

for i in range(m):
    a,b = map(int,input().split())
    l.append(a)
    r.append(b)

wall = [0] * (n+1)

for i in range(m):
    wall[l[i]-1] += 1
    wall[r[i]] -= 1
    
for i in range(1,n):
    wall[i] += wall[i-1]
    
min_wall = 1e10

for i in range(n):
    min_wall = min(min_wall,wall[i])

print(min_wall)