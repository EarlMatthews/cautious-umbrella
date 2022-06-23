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


# Test 00
print(uncompress("2c3a1t")) # -> 'ccaaat'

# Test 01
print(uncompress("4s2b")) # -> 'ssssbb'

# Test 02
print(uncompress("2p1o5p"))

# Test 03
print(uncompress("3n12e2z"))

# Test 04
print(uncompress("127y"))
