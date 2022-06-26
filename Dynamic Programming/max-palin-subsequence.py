def max_palin_subsequence(string):
    """
    Write a function, max_palin_subsequence, that takes in a string as an argument. 
    The function should return the length of the longest subsequence of the string that is also a palindrome.

    A subsequence of a string can be created by deleting any characters of the string, while maintaining the relative order of characters.
    """
    return _max_palin_subsequence(string,0,len(string) - 1,{})

def _max_palin_subsequence(string,i,j,memo):
    pos = (i,j)
    if pos in memo:
        return memo[pos]
    
    if i == j: # if I'm looking at a single character then it is a palindrome
        return 1 
    if i > j: # this is an empty string so return 0
        return 0
    
    if string[i] == string[j]:
        memo[pos] = 2 + _max_palin_subsequence(string, i+1, j-1,memo) 
        return memo[pos] # effectively removes both end of string if char match
    else:
        memo[pos] = max(_max_palin_subsequence(string, i + 1, j,memo), _max_palin_subsequence(string, i, j - 1,memo))
        return memo[pos]



#test_00:
print(max_palin_subsequence("luwxult")) # -> 5
#test_01:
print(max_palin_subsequence("xyzaxxzy")) # -> 6
#test_02:
print(max_palin_subsequence("lol")) # -> 3
#test_03:
print(max_palin_subsequence("boabcdefop")) # -> 3
#test_04:
print(max_palin_subsequence("z")) # -> 1
#test_05:
print(max_palin_subsequence("chartreusepugvicefree")) # -> 7
#test_06:
print(max_palin_subsequence("qwueoiuahsdjnweuueueunasdnmnqweuzqwerty")) # -> 15
#test_07:
print(max_palin_subsequence("enamelpinportlandtildecoldpressedironyflannelsemioticsedisonbulbfashionaxe")) # -> 31