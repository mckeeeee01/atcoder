n = int(input())

p = list(map(int, input().split()))
q = list(map(int, input().split()))


ans = []

for i in range(n):
    ans.append([q[i],q[p[i]-1]])
ans.sort()

for i in range(n):
    print(ans[i][1],end=" ")

print("")
