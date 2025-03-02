n = int(input())
a = list(map(int, input().split()))

flag = False
min_num = 1e6

ans_list = {}

for i in range(n):
    if a[i] in ans_list:
        flag = True
        min_num = min(min_num, i - ans_list[a[i]] + 1)
        ans_list[a[i]] = i
    else:
        ans_list[a[i]] = i

if flag:
    print(min_num)
else:
    print(-1)