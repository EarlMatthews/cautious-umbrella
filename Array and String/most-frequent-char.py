def most_frequent_char(s):
    count = char_count(s)
    most_frequent = s[0]
    for c in s:
        if count[c] > count[most_frequent]:
            most_frequent = c
    return most_frequent
  
def char_count(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1
    return count


print(most_frequent_char('bookeeper')) # -> 'e'
print(most_frequent_char('david')) # -> 'd'
print(most_frequent_char('abby')) # -> 'b'
print(most_frequent_char('mississippi')) # -> 'i'
print(most_frequent_char('potato')) # -> 'o'
print(most_frequent_char('eleventennine')) # -> 'e'
print(most_frequent_char('riverbed')) # -> 'r'