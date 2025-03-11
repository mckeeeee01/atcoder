n,m = map(int, input().split())

b = list(map(int, input().split()))
w = list(map(int, input().split()))

b.sort(reverse=True)
w.sort(reverse=True)


index_more_then_0 = sum(1 for x in b if x >= 0)
index_w = sum(1 for x in w if x >= 0)


new_array = []
ans = 0
if index_more_then_0 > index_w:
    for i in range(index_more_then_0):
        ans += b[i]
    for i in range(index_w):
        ans += w[i]
    print(ans)

    
else:
    for i in range(min(m,n)):
        new_array.append(b[i] + w[i])
    for i in range(len(new_array)):
        if new_array[i] >= 0:
            ans += new_array[i]
        else:
            break
    print(ans)
