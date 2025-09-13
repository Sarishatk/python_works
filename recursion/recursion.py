


# def count(n):
#     if n==0:
#         return
#     print(n)
#     return count(n-1)
# count(5)




def fact(n):

    if n==0:

        return 1
    
    return n*fact(n-1)

print(fact(5))



def sum_od_n(num):

    if num == 0:

        return 0
    return num+sum_od_n(num-1)

print(sum_od_n(5))