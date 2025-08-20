# find the largest number in the array

# arr = [10, 25, 3, 99, 56, 12]


arr = [10, 25, 3, 99, 56, 12]
largest_num = arr[0]
for num in arr:
    if largest_num < num:
        largest_num = num
print(f"the largest number is {largest_num}")



# Find the smallest number in an array
# arr = [8, -5, 0, 12, -20, 7]
# Expected: -20


