'''

befitting brackets
Write a function, befitting_brackets, that takes in a string as an argument. The function should return a boolean indicating whether or not the string contains correctly matched brackets.

You may assume the string contains only characters: ( ) [ ] { }
'''

def befitting_brackets(string):
	stack = []
	brackets = {
		'(': ')',
		'[': ']',
		'{': '}'
	}
	for c in string:
		if c in brackets:
			stack.append(brackets[c])
		else:
			if stack and stack[-1] == c:
				stack.pop()
			else:
				return False
	return len(stack) == 0


	print()

'''test_00:'''
print(befitting_brackets('(){}[](())')) # -> True

'''test_01:'''
print(befitting_brackets('({[]})')) # -> True

'''test_02:'''
print(befitting_brackets('[][}')) # -> False

'''test_03:'''
print(befitting_brackets('{[]}({}')) # -> False

'''test_04:'''
print(befitting_brackets('[]{}(}[]')) # -> False

'''test_05:'''
print(befitting_brackets('[]{}()[]')) # -> True

'''test_06:'''
print(befitting_brackets(']{}')) # -> False

'''test_07:'''
print(befitting_brackets('')) # -> True

'''test_08:'''
print(befitting_brackets("{[(}])")) # -> False