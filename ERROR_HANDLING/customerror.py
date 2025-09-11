def divide(num1,num2):

    if num2==0:

        raise Exception("num2 not be zero")
    else:
        return num1/num2
    
print(divide(10,0))