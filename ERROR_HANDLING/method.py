num1 = int(input("enter number1"))
num2= int(input("enter number2"))

try:
    div_res = num1/num2
    print(div_res)
except Exception as e:

    num2 = int(input("enter num2"))

    div_res = num1/num2

    print(div_res)

finally:
    print("send text message to user phone number")
    print("send email confirmation")









arr = [10,11,12,45,27,18,15]

index = int(input("enter index position > :"))

try:
    print(arr[index])
except Exception as e:
    print(e)

print("program completed")