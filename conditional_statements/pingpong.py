
# 1.check the number is ping,pomg or pingpong
num = int(input("enter a number : "))

if num%15==0 :

    print("PINGPONG")

elif num%3==0:

    print("PING")

elif num%5==0:

    print("PONG")



# 2.chcek the year ebd with 2 zeros or not

year = int(input("enter a year : "))

if year%100 ==0:
    print("ending with two zeros")
else:
    print("non centdury year")