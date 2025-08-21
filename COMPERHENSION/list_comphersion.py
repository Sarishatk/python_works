# comperhension
# easyest way to create list,set,dictonary  from an iterable
# syntax
# [experssion iterable condition]



         # example
    #  ------------------


fruits =["apple","banana","orange"]
upper_case = [item.upper() for item in fruits]
print(upper_case)


# arr = [2,3,4,56]
# find square list and cube list using compershion method

arr = [2,3,4,56]
cube_list = [num**3 for num in arr ]
print(cube_list)
square_list = [num**2 for num in arr]
print(square_list)
odd_numbers = [num for num in arr if num%2==0]
print(odd_numbers)



arr = [2,3,4,8,9,10]
# generate new list map num as num+1 if num>5 num-1

new_arr = [num+1 if num>5 else num-1 for num in arr]
print(new_arr)




# words = ["apple","banana","carrot","drumstich","egg","fissh"]
# create a news list of words starting with vowels
