


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