n = int(input())

c = []
l = []

for i in range(n):
    c_t,l_t = input().split()
    c.append(c_t)
    l.append(int(l_t))

length = 0
ans_str = ""
flag = False

for i in range(n):
    length += l[i]
    if length > 100:
        flag = True
        break
    ans_str += c[i] * l[i]
    
if flag:
    print("Too Long")
else:
    print(ans_str)
    
    
