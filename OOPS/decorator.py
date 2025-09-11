"""
 decorators are functions that is changed the behaviour of another fn without chnaging definition
 
"""
def decorator_fn(func):
    def wrapper(n1,n2):
        if n1<n2:
            n1,n2 = n2,n1
            return func(n1+n2)
        return wrapper




def sub(n1,n2):
    return n1 - n2

def add(n1 , n2):
    return n1+n2


print(add(3,4))
print(sub(4,5))
