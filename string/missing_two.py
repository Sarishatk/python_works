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
       
