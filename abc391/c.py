n,q = map(int, input().split())


num_pigeon = [1 for _ in range(n)]  #nest_index -> num_pigeon
pigeon_to_nest = [i for i in range(n)]  #pigeon_index -> nest_index

count = 0

for i in range(q):
	query = list(map(int, input().split()))
	if query[0] == 1:
		p,h = query[1],query[2]
		p,h = p-1,h-1
		if num_pigeon[pigeon_to_nest[p]] == 2:
			count -= 1
		num_pigeon[pigeon_to_nest[p]] -= 1
		num_pigeon[h] += 1
		pigeon_to_nest[p] = h
		if num_pigeon[h] == 2:
			count += 1

	else:
		print(count)
