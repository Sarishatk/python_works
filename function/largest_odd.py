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
