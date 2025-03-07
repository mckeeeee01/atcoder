n,q = map(int, input().split())

box_to_label = list(range(n))
label_to_box = list(range(n))
pigeon_to_box = list(range(n))

for _ in range(q):
	query = list(map(int, input().split()))
	query_type = query[0]
	if query_type == 1:
		pigeon, to = query[1], query[2]
		pigeon_to_box[pigeon - 1] = label_to_box[to - 1]
	elif query_type == 2:
		label0, label1 = query[1], query[2]
		label_to_box[label0 - 1], label_to_box[label1 - 1] = label_to_box[label1 - 1], label_to_box[label0 - 1]
		box_index0 = label_to_box[label0 - 1]
		box_index1 = label_to_box[label1 - 1]
		box_to_label[box_index0], box_to_label[box_index1] = box_to_label[box_index1], box_to_label[box_index0]
	else:  # query_type == 3
		pigeon = query[1]
		box_index = pigeon_to_box[pigeon - 1]
		label = box_to_label[box_index] + 1
		print(label)
