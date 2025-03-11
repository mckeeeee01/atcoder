n = int(input())
a = list(map(int, input().split()))

flag = False
for i in range(n-2):
    if a[i] == a[i+1] and a[i] == a[i+2]:
        flag = True

if flag:
    print("Yes")
else:
    print("No")


