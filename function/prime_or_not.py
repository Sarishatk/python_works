# craete a function is_prime with one parameter num
# return true if number is prime else false

# def prime_or_not(num):
#     is_prime = True
#     for i in range(2,num):
#         if num%i==0:
#             is_prime = False
#             break
#     return is_prime
# print(prime_or_not(5))

# create a function is_palindrome with one parameter num
# rerurn true if num is palindrome else return not palindrome

def is_palindrome(num):
    original = str(num)
    reverse = "".join(reversed(str(num)))
    if original == reverse:
        return True
    else:
        return False
print(is_palindrome(33))