q = int(input())

list_0 = [0] * 100

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        list_0.append(query[1])
    else:
        print(list_0[-1])
        list_0.pop()
