h,w = map(int, input().split())
s = [list(input()) for _ in range(h)]

width_max = 0
width_min = 1000

height_max = 0
height_min = 1000

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            height_max = max(height_max,i)
            height_min = min(height_min,i)
            width_max = max(width_max,j)
            width_min = min(width_min,j)

flag = True
            
for i in range(height_min,height_max+1):
    for j in range(width_min,width_max+1):
        if s[i][j] == ".":
            flag = False
            break

if flag:
    print("Yes")
else:
    print("No")
        