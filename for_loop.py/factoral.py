# num = int(input("enter a number : "))
# factorial = 1
# for i in range(1,num+1):
#     factorial = factorial*i
# print(factorial)


from random import randint
target = randint(1,11)
count = 0
while True:
    num = int(input("guess the number : "))
    count+=1
    if num == target:
        print(count,"times")
        print("congarts")
        