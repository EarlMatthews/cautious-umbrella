def compress(s):
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
