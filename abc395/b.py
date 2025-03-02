n = int(input())

num = (n+1)//2



grid = ["#" * n] * n
grid = [list(grid[i]) for i in range(n)]

count = 0
for i in range(num):
    count += 1
    for j in range(i, n-i):
        for k in range(i, n-i):
            if count % 2 == 0:
                grid[j][k] = "."
            else:
                grid[k][j] = "#"
    

for i in range(n):
    print(*grid[i], sep="")



