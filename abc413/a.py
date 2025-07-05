n,m = map(int,input().split())

a = list(map(int,input().split()))

a_sum = sum(a)

if a_sum > m:
    print("No")
else:
    print("Yes")
