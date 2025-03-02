n = int(input())
a = list(map(int, input().split()))

flag = True

for i in range(n-1):
    if a[i] >= a[i+1]:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")
