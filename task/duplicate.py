
# arr=[10,11,12,13,11,10,14]
# display duplicate number without any methods and operator



arr = [10, 11, 12, 13, 11, 10, 14]
duplicates = set()

for num in arr:
    if num in duplicates:
        print("dupliacte number is",num)
 
    else:
        duplicates.add(num)
    