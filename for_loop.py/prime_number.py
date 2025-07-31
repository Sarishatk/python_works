# check whether the number is prime or not

num = int(input("Enter a number : "))
is_prime = True
for i in range(2,num):
    if num%i == 0:
        is_prime = False
        break
result = "number is prime " if is_prime==True else "number is not prime" 
print(result)