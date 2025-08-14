
# arr=[10,11,12,13,11,10,14]
# display duplicate number without any methods and 'in' operator



arr = [10, 11, 12, 13, 11, 10, 14]
duplicates = []

# Loop up to len(arr) - 3 so arr[i + 3] is safe to access
for i in range(len(arr) - 3):
    if arr[i] == arr[i + 1]:
        duplicates.append(i)
    elif arr[i] == arr[i + 2]:
        duplicates.append(i)
    elif arr[i] == arr[i + 3]:
        duplicates.append(i)

print("Indices of duplicates:", duplicates)
