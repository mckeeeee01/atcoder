n,m = map(int, input().split())

s = [input() for _ in range(n)]
t = [input() for _ in range(m)]



for i in range(n - m + 1):
    for j in range(n - m + 1):
        flag = True
        for k in range(m):
            for l in range(m):
                if s[i+k][j+l] != t[k][l]:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            print(i+1,j+1)
            exit()
