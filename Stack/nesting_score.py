'''
nesting score
Write a function, nesting_score, that takes in a string of brackets as an argument. The function should return the score of the string according to the following rules:

[] is worth 1 point
XY is worth m + n points where X, Y are substrings of well-formed brackets and m, n are their respective scores
[S] is worth 2 * k points where S is a substring of well-formed brackets and k is the score of that substring
You may assume that the input only contains well-formed square brackets.

'''

def nesting_score(string):
	stack = [0]
	for c in string:
		if c == '[' : 
			stack.append(0)
		if c == ']' :
			item = int(stack.pop())
			if item == 0:
				stack[-1] += 1
			else:
					stack[-1] += 2 * item
	return stack[0]

print(nesting_score('[[][][][]][]'))

'''test_00:'''
print(nesting_score("[]")) # -> 1

'''test_01:'''
print(nesting_score("[][][]")) # -> 3

'''test_02:'''
print(nesting_score("[[]]")) # -> 2

'''test_03:'''
print(nesting_score("[[][]]")) # -> 4

'''test_04:'''
print(nesting_score("[[][][]]")) # -> 6

'''test_05:'''
print(nesting_score("[[][]][]")) # -> 5

'''test_06:'''
print(nesting_score("[][[][]][[]]")) # -> 7

'''test_07:'''
print(nesting_score("[[[[[[[][]]]]]]][]")) # -> 129