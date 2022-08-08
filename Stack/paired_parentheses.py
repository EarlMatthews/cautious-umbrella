'''
paired parentheses
Write a function, paired_parentheses, that takes in a string as an argument. The function should return a boolean indicating whether or not the string has well-formed parentheses.

You may assume the string contains only alphabetic characters, '(', or ')'.

'''


def paired_parentheses(string):
	count = 0
	for c in string:
		if c == '(':
			count += 1
		if c == ')':
			count -= 1
		if count < 0:
			return False
	if count == 0:
		return True
	return False


''' Tests '''

'''test_00:'''
print(paired_parentheses("(david)((abby))")) # -> True

'''test_01:'''
print(paired_parentheses("()rose(jeff")) # -> False

'''test_02:'''
print(paired_parentheses(")(")) # -> False
'''test_03:'''
print(paired_parentheses("()")) # -> True
'''test_04:'''
print(paired_parentheses("(((potato())))")) # -> True
'''test_05:'''
print(paired_parentheses("(())(water)()")) # -> True
'''test_06:'''
print(paired_parentheses("(())(water()()")) # -> False
'''test_07:'''
print(paired_parentheses("")) # -> True
'''test_08:'''
print(paired_parentheses("))()")) # False