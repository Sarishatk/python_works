# greatest of two numbers

# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# if num1>num2:
#     print(num1,"is greater than ",num2)
# else:
#     print(num2,"is greate than",num1)


# =====================================================

# greatest among three numbers

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))
if num1>num2 and num1>num3:
    print(num1 ,"is greater")
elif num2>num1 and num2>num3:
    print(num2,"is greater")
else:
    print(num3,"is greater")