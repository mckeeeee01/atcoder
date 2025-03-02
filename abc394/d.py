s = input()

color_list = ["(", ")", "[","]", "{","}"]

color_number = [0,0,0,0,0,0]

for i in range(len(s)):
	if s[i] == "(":
		color_number[0] += 1
	elif s[i] == ")":
		color_number[1] += 1
	elif s[i] == "[":
		color_number[2] += 1
	elif s[i] == "]":
		color_number[3] += 1
	elif s[i] == "{":
		color_number[4] += 1
	elif s[i] == "}":
		color_number[5] += 1
	
	if color_number[0] - color_number[1] < 0 or \
	color_number[2] - color_number[3] < 0 or \
	color_number[4] - color_number[5] < 0 or \
	
    :
		print("NO")
		exit()

if color_number[0] == 0 and color_number[1] == 0 and color_number[2] == 0:
	print("YES")
else:
	print("NO")
