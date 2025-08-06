# craete a function is_prime with one parameter num
# return true if number is prime else false

def prime_or_not(num):
    is_prime = True
    for i in range(2,num):
        if i%2==0:
            is_prime = False
            break
    return is_prime
print(prime_or_not(3))

