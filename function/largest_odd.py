# crate a function that will return largest odd number with one param
# that will return largest odd number from num

def largest_odd_number(num):
    while num!=0:
        digit = num % 10
        if digit%2!=0:
            print(num)
            break
        num = num //10
largest_odd_number(234)



# create a function with odd even count  with one parameter number 
# fn display count of  odd number and count of even number


def odd_even(num):
    odd_count=0
    even_count=0
    while num!=0:
        digit = num %10
        if digit%2 == 0:
            even_count+=1
        else:
            odd_count+=1
        num = num // 10
    print("odd count is", odd_count)
    print("even count is ", even_count)

odd_even(1234)
        



