
 # arr=[153,151,1634,1771,2332]

# generate three new list palindrome_list and armstrong_list,prime_number

arr=[153,151,1634,1771,2332]
palindrome = []
armstrong = []
prime = []
for array in arr:
    reverse = str(array)
    reverse2 = "".join(reversed(reverse))
    if reverse2 == reverse:
       palindrome.append(array)
print(palindrome)
        
        


