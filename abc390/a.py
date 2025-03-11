a = list(map(int, input().split()))

flag = False
for i in range(4):
    a_copy = a.copy()
    a_copy[i], a_copy[i+1] = a_copy[i+1], a_copy[i]
    if a_copy == [1,2,3,4,5]:
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")
