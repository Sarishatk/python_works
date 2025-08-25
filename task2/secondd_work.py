# First Repeated Character
# Input: "programming


word = "programming"
reapted_character = set()
for i in word:
    if i in reapted_character:
        print("the first repeated character is ",i)
        break
    else:
        reapted_character.add(i)


# Generate First N Prime Numbers (starting from 13)
# Input: 5 → Output: 13, 17, 19, 23, 29
n = 5
primes = []
start = 13
num = start

while len(primes)<n:
    is_prime = True
    if num < 2:
        is_prime = False
    else:

        for i in range(2,num):
            if num % i == 0:
                is_prime = False
                break
    if is_prime:
        primes.append(num)
    num +=1
print(primes)


# Find Factorial of a Number
# Input: 5 → Output: 120

num = int(input("enter the number"))
fact = 1
for i in range(1,num+1):
    fact = fact*i
print(fact)
    

# Check Armstrong Number
# Input: 153 → Output: True (since 1³+5³+3³=153)

number = 153
sum = 0
while number!=0:
    last_digit = num % 10
    cube = last_digit**3
    sum +=cube
    number//10
print(sum)



# Find GCD of Two Numbers
# Input: 48, 18 → Output: 6



