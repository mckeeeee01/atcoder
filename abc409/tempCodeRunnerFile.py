n = int(input())
t = input()
a = input()


for i in range(n):
    if t[i] == a[i]:
        print("Yes")
        exit()

print("No")
