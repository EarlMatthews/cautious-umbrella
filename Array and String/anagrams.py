# def anagrams(s1, s2):
#   return sorted(s1) == sorted(s2)

def anagrams(s1,s2):
  return char_count(s1) == char_count(s2)

def char_count(s):
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