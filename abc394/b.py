N = int(input())

s = []

for i in range(N):
    s.append(input())
    
len_list = []
for i in range(N):
	len_list.append([len(s[i]),i])
 
len_list.sort()

ans = ""

for i in range(N):
    ans += s[len_list[i][1]]
    
print(ans)