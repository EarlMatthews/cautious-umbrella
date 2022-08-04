# def anagrams(s1, s2):
# 	'''
# 	This works and only requires one line
# 	Time complexity for Tim sort is O(n) and 
# 	Space Complexity is O(n)
# 	'''
# 	return sorted(s1) == sorted(s2)

def anagrams(s1,s2):
	"""
	Uses helper function char_count(s) to store 
	"""
	return char_count(s1) == char_count(s2)

def char_count(s):
	'''
	Use dictionary for constant time comparison of items to dictionary
	'''
	count = {}
	for char in s:
		if char not in count:
			count[char] = 0
		count[char] += 1
	return count

print(anagrams('restful', 'fluster'))           # -> True
print(anagrams('cats', 'tocs'))                 # -> False
print(anagrams('monkeyswrite', 'newyorktimes')) # -> True
print(anagrams('paper', 'reapa'))               # -> False
print(anagrams('elbow', 'below'))               # -> True
print(anagrams('tax', 'taxi'))                  # -> False
print(anagrams('taxi', 'tax'))                  # -> False
print(anagrams('night', 'thing'))               # -> True
print(anagrams('abbc', 'aabc'))                 # -> False