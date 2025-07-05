n = int(input())

str_list = []

for i in range(n):
    str_list.append(input())

ans_set = set()
for i in range(n):
    for j in range(n):
        if i != j:
            ans_set.add(str_list[i]+str_list[j])

print(len(ans_set))
