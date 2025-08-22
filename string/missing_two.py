list = [1,2,3,5,6]

for i in range(len(list)-1):
    j = i+1
    differnce = list[j] - list[i]
    if differnce!=1:
        print(list[i]+1,"is missing")
        break



# arr = [10, 11, 12, 14, 15]
# Find and print the missing number in the sequence.


arr = [10, 11, 12, 14, 15]                           
for i in range(len(arr)-1):
    j = i+1
    differnce = arr[j] - arr[i]
    if differnce!=1:
        print(arr[i]+1,"is missed")
        break



# arr = [1, 2, 4, 6, 7, 9]
# Print all the missing numbers between the first and last element.
# (Expected: 3, 5, 8)



arr = [1, 2, 4, 6, 7, 9] 
missin_no = []                         
for i in range(len(arr)-1):
    j = i+1
    differnce = arr[j] - arr[i]
    if differnce!=1:
        for k in range(1,differnce):
            missin_no.append(arr[i]+1)
            
print(missin_no)



# arr = [2, 5, 3, 7, 5, 9, 2]
# Print the first number that is repeated.
# (Expected: 5)

arr = [2, 5, 3, 7, 5, 9, 2]
dupli = set()
for num in arr:
    if num in dupli:
        print("the first reparated chartacter is ",num)
        break
    else:
        dupli.add(num)


# arr = [3, 2, 5, 4, 7, 8, 6]
# Print all numbers that are greater than the number before them.
# (Expected: 5, 7, 8)


arr = [3, 2, 5, 4, 7, 8, 6]
greater_no = []
for i in range(1,len(arr)):
    if arr[i]>arr[i-1]:
        greater_no.append(arr[i])
print(greater_no)

arr = [3, 2, 5, 4, 7, 8, 6]
greater_no = []
for i in range(1,len(arr)):
    j = 1+1
    if arr[i]>arr[j]:
        greater_no.append(arr[i])
    
print(greater_no)

