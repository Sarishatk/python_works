colors = {"s":"success","d":"danger","o":"orange","g":"green"}
print(colors.get("d"))
print(colors.keys())
print(colors.pop("d"))
print(colors)


#  'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']


# number =  [2,3,4,5,6]
# square_dict ={2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
numbers = [2,3,4,5,6]
square_dict = {}
for num in numbers:
    square_dict[num] = num **2
print(square_dict)



text = "goodmorning"
char_count = {}
for w in text:
    if w in char_count:
        char_count[w]+=1
    else:
        char_count[w]=1
print(char_count)



# 2nd method

text = "goodmorning"
char_count ={}
for ch in set(text):
    char_count[ch] = text.count(ch)
print(char_count)

max_frequency = 0
max_frequency_dictionary = {}
for k,v in char_count.items():
    if v>max_frequency:
        max_frequency = v
        max_frequency_dictionary.clear()
        max_frequency_dictionary[k]=v
print(max_frequency_dictionary)
