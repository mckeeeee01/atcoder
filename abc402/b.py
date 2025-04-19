q = int(input())

query = 0
menu = []
for i in range(q):
    query = input().split()
    if query[0] == "1":
        menu.append(query[1])
    else:
        if len(menu) != 0:
            print(menu[0])
            menu.pop(0)
