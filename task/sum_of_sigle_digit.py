# 1.	Sum of Digits Until Single Digit


num = int(input("Enter a number: "))

while num >= 10: 
    sum_digits = 0
    while num != 0:
        sum_digits += num % 10
        num = num // 10
    num = sum_digits  

print("Single digit sum:", num)
