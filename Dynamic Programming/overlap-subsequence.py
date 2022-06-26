def overlap_subsequence(string_1, string_2):
    """
    Write a function, overlap_subsequence, that takes in two strings as arguments. 
    The function should return the length of the longest overlapping subsequence.

    A subsequence of a string can be created by deleting any characters of the string,
    while maintaining the relative order of characters.
    """
    return _overlap_subsequence(string_1, string_2,0,0,{})

def _overlap_subsequence(string_1, string_2,i,j, memo):
    pos = (i,j)
    if pos in memo:
        return memo[pos]
    
    if i == len(string_1) or j == len(string_2): # check if either string is empty
        return 0
    
    if string_1[i] == string_2[j]:
        memo[pos] = 1 + _overlap_subsequence(string_1, string_2,i+1,j+1,memo)
        return memo[pos]
    else:
        memo[pos] = max(_overlap_subsequence(string_1, string_2,i+1,j, memo), _overlap_subsequence(string_1, string_2,i,j+1, memo))
        return memo[pos]


#test_00:
print(overlap_subsequence("dogs", "daogt")) # -> 3
#test_01:
print(overlap_subsequence("xcyats", "criaotsi")) # -> 4
#test_02:
print(overlap_subsequence("xfeqortsver", "feeeuavoeqr")) # -> 5
#test_03:
print(overlap_subsequence("kinfolklivemustache", "bespokekinfolksnackwave")) # -> 11
#test_04:
print(overlap_subsequence(
  "mumblecorebeardleggingsauthenticunicorn",
  "succulentspughumblemeditationlocavore"
)) # -> 15
