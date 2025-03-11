n = int(input())
a = list(map(int, input().split()))

flag = True
for i in range(n-1):
    for j in range(i+1, n-1):
        if a[i+1]*a[j] != a[j+1]*a[i]:
            flag = False
            break
    if not flag:
        break

if flag:
    print("Yes")
else:
    print("No")