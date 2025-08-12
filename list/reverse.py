# num = [1,23,564,4]
# num.sort(reverse=True)
# print(num)


arr = [1,10,11,12,34,35]
# create a new array odd_arr, and even_arr
even_arr = []
odd_arr = []
for arr1 in arr:
    if arr1%2 ==0:
        even_arr.append(arr1)
    else:
        odd_arr.append(arr1)
print(odd_arr)
print(even_arr)