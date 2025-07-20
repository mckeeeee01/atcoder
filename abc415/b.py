s = input()

tmp = 0

for i in range(len(s)):
    if s[i] == "#":
        if tmp % 2 == 0:
            tmp += 1
            print(i+1, end=",")
        else:
            tmp += 1
            print(i+1, end="\n")
