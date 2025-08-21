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

arr = [8, -5, 0, 12, -20, 7]
positive = []
negative = []
for num in arr:
    if num>0:
        positive.append(num)
    else:
        negative.append(num)
print("the smallest number is :",(min(negative)))

# another method
arr = [8, -5, 0, 12, -20, 7]

arr_sorted = sorted(arr) 
print("The smallest number is:", arr_sorted[0])



# Find the second largest number in an array

# arr = [10, 20, 4, 45, 99]
# Expected: 45



arr = [10, 20, 4, 45, 99]
sorted_arr = sorted(arr)
print(f"second largest element is {sorted_arr[3]}")




# Find the number closest to 100 in a list

# arr = [85, 120, 95, 150, 102, 99]
# Expected: 99 (since it is closest to 100)


arr = [85, 120, 95, 150, 102, 99]

target = 100

before_target = []
after_target = []
for num in arr:
    if num > target:
        after_target.append(num)
    else:
        before_target.append(num)
print("the number closest to 100 is",max(before_target))

# another method
arr = [85, 120, 95, 150, 102, 99]
target = 100

closest = arr[0]
for num in arr:
    if abs(num - target) < abs(closest - target):
        closest = num

print("The number closest to 100 is:", closest)
