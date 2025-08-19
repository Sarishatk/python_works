# colors = {"s":"success","d":"danger","o":"orange","g":"green"}
# # print(colors.get("d"))
# # print(colors.keys())
# print(colors.pop("d"))
# print(colors)


#  'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']


# number =  [2,3,4,5,6]
# square_dict ={2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
numbers = [2,3,4,5,6]
square_dict = {}
for num in numbers:
    square_dict[num] = num **2
print(square_dict)
