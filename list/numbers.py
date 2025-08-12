# arr =[1,2,3,4,5,6,7,8,9,10,12] 
# display all even numbers from list


# arr =[1,2,3,4,5,6,7,8,9,10,12]
# for i in arr:
#     if i%2==0:
#      print(f"even  {i}")


# arr =[1,2,3,4,5,6,7,8,9,10,12] 
# display all odd numbers from list


# arr =[1,2,3,4,5,6,7,8,9,10,12]
# for i in arr:
#     if i%2!=0:
#        print(f"odd  {i}")
    

# years =[1900,1901,1991,1992,1993,1994,2000,2024,2021,2011] 
# display all leap years from list

# years =[1900,1901,1991,1992,1993,1994,2000,2024,2021,2011] 
# for yr in years:
#    if yr%4==0 and yr%100!=0 or yr%400==0:
#       print(yr)


#  numbers=[151,152,153,1634,8891,345,678]
# display armstrong numbers from list

numbers=[151,152,153,1634,8891,345,678]
for num in numbers:
   original = num 
   sum = 0
   length = len(str(num))
   while num!=0:
    digit = num % 10
    square = digit**length 
    sum+=square
    num = num // 10
   if original == sum:
      print(f'Armstrong numbers is {sum}')
   


# numbers =[11,12,13,33,131,343,12321,1234]
# display palindromic numbers from list


