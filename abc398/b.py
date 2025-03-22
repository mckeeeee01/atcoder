a = list(map(int, input().split()))


card = [0] * 13

for i in a:
    card[i-1] += 1
    
flag1 = False
flag2 = False
for i in range(13):
    if card[i] >= 3:
        flag1 = True
        card[i] = 0
        break

for i in range(13):
    if card[i] >= 2:
        flag2 = True

if flag1 and flag2:
    print("Yes")
else:
    print("No")