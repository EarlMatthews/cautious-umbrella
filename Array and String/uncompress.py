def uncompress(s):
	result = ""
	i = 0
	for j in range(len(s)):
		if s[j].isalpha():
			num = int(s[i:j])
			char = s[j]
			result += num * char
			i = j+1
	return result