a,b = map(int, input().split())

if a/b - a//b > 0.5:
    print(a//b + 1)
else:
    print(a//b)