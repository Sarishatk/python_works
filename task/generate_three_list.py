
 # arr=[153,151,1634,1771,2332]

# generate three new list palindrome_list and armstrong_list,prime_number
arr = [153, 151, 1634, 1771, 2332]
palindrome = []
armstrong = []
prime = []

for array in arr:
    # palindrome
    reverse = str(array)
    reverse2 = "".join(reversed(reverse))
    if reverse2 == reverse:
        palindrome.append(array)

    # armstrong
    original = array
    total = 0
    temp = array  
    while temp != 0:
        digit = temp % 10
        total += digit ** len(str(original))
        temp //= 10
    if total == original:
        armstrong.append(original)


    # prime or not
  
    is_prime = True
    for i in range(1, int(array ** 0.5) + 1):
            if array % i == 0:
                is_prime = False
                break
    if is_prime:
            prime.append(array)

print("Palindromes:", palindrome)
print("Armstrong numbers:", armstrong)
print("prime number is",prime)



