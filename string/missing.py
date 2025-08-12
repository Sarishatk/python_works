# find least + ve missing number from this sorted array start from 1

arr = [1, 2, 4, 5]

missing_no = None
for i in range(1,len(arr)+2):
    if i not in arr:
        missing_no = i
        break
print(f"least positive missing number {missing_no}")


# 2nd method of finding least postive missing number