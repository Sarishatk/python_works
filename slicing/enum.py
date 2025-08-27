arr = [10,11,12,13]
for index,num in enumerate(arr):
    print(index,num)


lst = [2,3,4,5,6]
for index,element in enumerate(lst,start=1):
    print(element**index,end="")