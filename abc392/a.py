a1,a2,a3 = map(int, input().split())

flag = False
if a1 * a2 == a3:
	flag = True
if a1 * a3 == a2:
	flag = True
if a2 * a3 == a1:
	flag = True

if flag:
	print("Yes")
else:
	print("No")

