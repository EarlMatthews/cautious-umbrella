def compress(s):
    """
    Problem: Write a function, compress, that takes in a string as an argument. 
    The function should return a compressed version of the string where consecutive
     occurrences of the same characters are compressed into the number of occurrences followed by the character. 
    Single character occurrences should not be changed.
    Uses 2 moving pointers i,j 
    """
    i = 0
    j = 0
    s_prime = s + '!' #add char so that last char is always unique
    result = []
    while j < len(s_prime):
        if s_prime[i] != s_prime[j]:
            count = j - i
            if count == 1:
                result.append(s_prime[i])
            else:
                result.append(str(count) + s_prime[i])
            i = j
        j = j + 1
    return ''.join(result)
    
test_string = "ccaaatsss"
print(compress(test_string))

print(compress('ssssbbz')) # -> '4s2bz'
print(compress('ppoppppp')) # -> '2po5p'
print(compress('nnneeeeeeeeeeeezz')) # -> '3n12e2z'
