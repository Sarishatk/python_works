# chck the number is armstrong or not

num = int(input("enter a armstrong number :"))
original = num
sum = 0
while num!=0:
    digit = num % 10
    cube = digit**3
    sum += cube
    num = num // 10
if sum == original :
    print(original,"is a armstrong number")
else:
    print(original,"not a armstrong number")