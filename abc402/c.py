n,m = map(int, input().split())

ka = []

for i in range(m):
    tmp = list(map(int, input().split()))
    ka.append(tmp)

b = list(map(int, input().split()))


#一番最後に克服する食材を考えればよい
#全探索はTLE
#Biの順にソートできれば簡単にできる
#