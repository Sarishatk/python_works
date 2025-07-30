
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




# print digit count

num = 876876
counter = 0
while num!=0:
    digit = num % 10
    counter+=1
    num = num // 10
print(counter)