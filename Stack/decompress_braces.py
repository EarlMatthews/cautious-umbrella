'''
decompress braces
Write a function, decompress_braces, that takes in a compressed string as an argument. The function should return the string decompressed.

The compression format of the input string is 'n{sub_string}', where the sub_string within braces should be repeated n times.

You may assume that every number n is guaranteed to be an integer between 1 through 9.

You may assume that the input is valid and the decompressed string will only contain alphabetic characters.

'''

def decompress_braces(string):
	number_chars = '123456789'
	stack = []
	for char in string:
		if char in number_chars:
			stack.append(int(char))
		else:
			if char == '}':
				segment = ''
				while not isinstance(stack[-1], int):
					popped = stack.pop()
					segment = popped + segment
				num = stack.pop()
				stack.append(segment * num)
				
			elif char != '{':
				stack.append(char)
	return ''.join(stack)
	

'''test_00:'''
print(decompress_braces("2{q}3{tu}v"))
# -> qqtututuv 

'''test_01:'''
print(decompress_braces("ch3{ao}"))
# -> chaoaoao

'''test_02:'''
print(decompress_braces("2{y3{o}}s"))
# -> yoooyooos

'''test_03:'''
print(decompress_braces("z3{a2{xy}b}"))
# -> zaxyxybaxyxybaxyxyb 

'''test_04:'''
print(decompress_braces("2{3{r4{e}r}io}"))
# -> reeeerreeeerreeeerioreeeerreeeerreeeerio 

'''test_05:'''
print(decompress_braces("go3{spinn2{ing}s}"))
# -> gospinningingsspinningingsspinningings 

'''test_06:'''
print(decompress_braces("2{l2{if}azu}l"))
# -> lififazulififazul 

'''test_07:'''
print(decompress_braces("3{al4{ec}2{icia}}"))
# -> alececececiciaiciaalececececiciaiciaalececececiciaicia 