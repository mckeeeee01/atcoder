n,s = map(int,input().split())

t = list(map(int,input().split()))



for i in range(n):
    if i == 0:
        if t[0] > s:
            print("No")
            exit()
    else:
        if t[i] - t[i-1] > s:
            print("No")
            exit()

print("Yes")
