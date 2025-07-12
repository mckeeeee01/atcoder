n,l,r = map(int, input().split())

x = []
y = []

for i in range(n):
    x_t,y_t = map(int, input().split())
    x.append(x_t)
    y.append(y_t)

count = 0

for i in range(n):
    if x[i] <= l and r <= y[i]:
        count += 1

print(count)
