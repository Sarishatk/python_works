# find least + ve missing number from this sorted array start from 1

arr = [1, 2, 4, 5]

missing_no = None
for i in range(1,len(arr)+2):
    if i not in arr:
        missing_no = i
        break
print(f"least positive missing number {missing_no}")


# 2nd method of finding least postive missing number


arr = [1, 2, 4, 5]
for i in range(len(arr)-1):
    j=arr[i]+1
if arr[i+1] - arr[i] != 1:
      print("the leat cost positive integer is ",j)


# q3

# arr=[10,11,12,13,11,10,14]
# display duplicate number without any methods and 'in' operator

arr=[10,11,12,13,11,10,14]
duplicate_elements = []
for i in range(len(arr)-1):
     j=arr[i]+1
     if arr[i+1]==arr[i]:
          duplicate_elements.append(i)
print(duplicate_elements)