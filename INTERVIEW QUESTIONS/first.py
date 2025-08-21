# given an array of numbers find the closet number to zero


# method1
arr = [-2,-3,-4,-1,2,3,4,5,1]
for num in arr:
    if num>-1 and num<2:
        print(f"the closest number is {num}")



        
# method2
arr = [-2, -3, -4, -1, 2, 3, 4, 5, 1]

closest = arr[0]   
for num in arr:
    if abs(num) < abs(closest):
        closest = num
        if closest < 0  and abs( closest) in arr:
            closest = abs(closest)

print("The closest number to zero is:", closest)

