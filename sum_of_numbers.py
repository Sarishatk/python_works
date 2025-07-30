
# set number 
# set sum 
# loop
  #extract last digit
  #add last digit with sum
  # remove last digit from number
# print sum
   

num = 5643
sum = 0
while num!=0:
    last_digit = num % 10
    sum+=last_digit
    num = num // 10
print(sum)