from collections import deque

q = int(input())

int_array = deque()

for i in range(q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        int_array.append([query[2],query[1]])
    else:
        output = 0
        counter = query[1]
        while counter > 0:
            # この要素は全てなくなる場合
            if int_array[0][1] < counter:
                output += int_array[0][0] * int_array[0][1]
                counter -= int_array[0][1]
                int_array.popleft()
            # この要素は一部なくなる場合
            else:
                output += int_array[0][0] * counter
                int_array[0][1] -= counter
                break
        print(output)
