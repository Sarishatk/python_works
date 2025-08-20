# find the largest number in the array

# arr = [10, 25, 3, 99, 56, 12]


arr = [10, 25, 3, 99, 56, 12]
largest_num = arr[0]
for num in arr:
    if largest_num < num:
        largest_num = num
print(f"the largest number is {largest_num}")