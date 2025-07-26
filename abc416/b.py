s = input()


isSharp = True

t = ''

for i in range(len(s)):
    if s[i] == '#':
        isSharp = True
        t += '#'
        continue
    if isSharp:
        t += 'o'
        isSharp = False
    else:
        t += '.'

print(t)