n,l,r = map(int,input().split())

s = input()

flag = True

for i in range(l-1,r):
    if s[i] != 'o':
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")