n = int(input())
a = list(map(int, input().split()))


left_list = [0] * (n-1)
right_list = [0] * (n-1)

set_left = set()
set_right = set()


for i in range(n-1):
    set_left.add(a[i])
    left_list[i] = len(set_left)

ans = []
for i in range(n-1):
    set_right.add(a[n-1-i])
    right_list[i] = len(set_right)

for i in range(n-1):
    ans.append(left_list[i] + right_list[n-2-i])

print(max(ans))