import math

n,m = map(int, input().split())
a = []
b = []

diff = [0] * (n + 1)

for _ in range(m):
    tmpa,tmpb = map(int, input().split())
    a.append(tmpa)
    b.append(tmpb)
    if tmpa + tmpb > n:
        diff[tmpa + tmpb - n] += 1
    else:
        diff[tmpa + tmpb] += 1
        
    
diff_count = 0
for i in range(len(diff)):
    if diff[i] >= 2:
        diff_count += math.comb(diff[i],2)
        
print(math.comb(m,2) - diff_count)