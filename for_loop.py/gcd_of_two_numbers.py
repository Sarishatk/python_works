# find the greatest commom divisor

first_no = int( input("Enter first number : "))
last_no = int( input("Enter last number : "))
limit = min(first_no, last_no)
for i in range(1,limit+1):
    if first_no % i == 0 and last_no % i == 0:
        print(i)