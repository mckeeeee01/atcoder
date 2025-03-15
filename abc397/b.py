s = input()


l = len(s)

count = 0

flag = True
for i in range(l):
    if flag:
        if s[i] == "o":
            count += 1
        else:
            flag = False
    else:
        if s[i] == "i":
            count += 1
        else:
            flag = True
        
if (l % 2 == 1 and count % 2 == 0) or (l % 2 == 0 and count % 2 == 1): 
    count += 1
        
print(count)  
