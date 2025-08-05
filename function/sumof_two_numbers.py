# def sum_of_numbers(num1,num2):
#     result = num1+num2
#     return result
# print(sum_of_numbers(100,200))


# enter 2 numbers and compare last digit od num1 > num2 

def last_digit(num1,num2):
    last_digit_num1 = num1 % 10
    last_digit_num2 = num2 % 10
    if last_digit_num1 > last_digit_num2:
        return num1
    else:
        return num2
print(last_digit(192,187))

# simplest way

def last_digit(num1,num2):
    return num1 if num1%10 > num2%10 else num2
print(last_digit(234,232))