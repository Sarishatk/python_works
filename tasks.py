# q1 => read start and stop display all numbers from start to stop

# start = int(input("Enetr starting number : "))
# stop =  int(input("Enetr stoping number : "))
# for i in range(start,stop+1):
#     print(i)

# 2nd method 
# start = int(input("Enetr starting number : "))
# stop =  int(input("Enetr stoping number : "))
# while start<=stop:
#     print(start)
#     start+=1


# =====================================================

#q2 => display all even number from 1 to 100

# for i in range(0,101,2):
#     print(i)

# start = 1
# stop = 100

# while start <= stop:
#     if start % 2 == 0:
#         print(start)
#     start += 1


# ========================================================


#q3 => display all ood numbers from 1 to 100
# start = 1
# stop = 100


# while start <= stop:
#     if start % 2 != 0:
#         print(start)
#     start += 1
# ============================================================


# q4 => display all century years from 1879 to 2026



# q5 => dispaly all non century years from 1879 to 2026



# q6 => diaplay all leap years from 1879 to 2026
start = 1879
stop = 2026

while start < stop:
    if (start % 4 == 0 and start % 100 != 0) or (start % 400 == 0):
        print(start)
    start += 1