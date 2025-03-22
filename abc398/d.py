n,r,c = map(int, input().split())
s = input()

center = [0,0] #smoke made in the center

first = [r,c] # where he is now

true_list = set()
true_list.add(tuple(center))


for si in s:
    if si == "E":
        center[1] -= 1
        first[1] -= 1
    elif si == "W":
        center[1] += 1
        first[1] += 1
    elif si == "N":
        center[0] += 1
        first[0] += 1
    else:
        center[0] -= 1
        first[0] -= 1

    true_list.add(tuple(center))
    if tuple(first) not in true_list:
        print("0", end="")
    else:
        print("1", end="")
        
print()
