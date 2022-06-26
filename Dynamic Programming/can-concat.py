def can_concat(s, words):
    """
    Write a function, can_concat, that takes in a string and a list of words as arguments. 
    The function should return boolean indicating whether or not it is possible to 
    concatenate words of the list together to form the string.

    You may reuse words of the list as many times as needed.
    """
    return _can_concat(s, words,{})

def _can_concat(s, words, memo):
    if s in memo:
        return memo[s]
    if s == '':
        return True
    for word in words:
        if s.startswith(word):
            suffix = s[len(word):]
            if _can_concat(suffix, words, memo) == True:
                memo[s] = True
                return True
    memo[s] = False
    return False


#test_00:
print(can_concat("oneisnone", ["one", "none", "is"])) #  -> True
#test_01:
print(can_concat("oneisnone", ["on", "e", "is"])) #  -> False
#test_02:
print(can_concat("oneisnone", ["on", "e", "is", "n"])) #  -> True
#test_03:
print(can_concat("foodisgood", ["is", "g", "ood", "f"])) #  -> True
#test_04:
print(can_concat("santahat", ["santah", "hat"])) #  -> False
#test_05:
print(can_concat("santahat", ["santah", "san", "hat", "tahat"])) #  -> True
#test_06:
print(can_concat("rrrrrrrrrrrrrrrrrrrrrrrrrrx", ["r", "rr", "rrr", "rrrr", "rrrrr", "rrrrrr"])) #  -> False