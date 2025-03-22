from collections import deque

n = int(input())
a = list(map(int, input().split()))
index_list = a

a = sorted(a, reverse = True)
a = deque(a)

while True:
    if len(a) == 0:
        print(-1)
        exit()
    del_word = a[0]
    
    del_flag = False  
    while True:
        if len(a) == 0:
            print(-1)
            exit()
        if len(a) == 1:
            if del_flag:
                if a[0] == del_word:
                    print(-1)
                    exit()
                else: #a[0] != del_word
                    print(index_list.index(a[0])+1)
                    exit()
            else: #del_flag == False
                print(index_list.index(a[0])+1)
                exit()
        if del_word == a[1]:
            del_flag = True
            a.popleft()
            if len(a) == 0:
                print(-1)
                exit()
        else:
            if del_flag:
                a.popleft()           
            break

    if len(a) == 1:
        print(index_list.index(a[0])+1)
        exit()
    if len(a) == 0:
        print(-1)
        exit()
    if a[0] > a[1]:
        print(index_list.index(a[0])+1)
        exit()
