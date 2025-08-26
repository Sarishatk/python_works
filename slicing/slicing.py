# definition
"""
slicing means extracting a part (subsequence) from a sequence 
like a list,string, or tuple using a special syntax
"""




word = "sarisha"
slice_word = word[5:]
print(slice_word)



word = "luminar"
slice = word[::-1]
print(slice)



arr = ["word","madam","racecar" ,"car"]
for w in arr:
    if w == w[::-1]:
        print(w)



