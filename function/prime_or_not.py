# craete a function is_prime with one parameter num
# return true if number is prime else false

def prime_or_not(num):
 is_prime = True
 for i in range(2,num):
    if num%i == 0:
        is_prime = False
        break
 result = "number is prime " if is_prime==True else "number is not prime" 
 return result
print(prime_or_not(4))

