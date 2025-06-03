n = int(input())
a = list(map(int,input().split()))


ans = set(a)

ans = list(ans)

ans.sort()

print(len(ans))
print(*ans)

