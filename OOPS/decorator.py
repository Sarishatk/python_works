"""
 decorators are functions that is changed the behaviour of another fn without chnaging definition
 
"""
def decorator_fn(func):
    def wrapper(n1,n2):
        if n1<n2:
           ( n1,n2) = (n2,n1)
        return func(n1,n2)
    return wrapper
              



@decorator_fn
def sub(n1,n2):
    return n1 - n2
@decorator_fn
def add(n1 , n2):
    return n1+n2


print(add(6,4))
print(sub(4,5))



def abs_dec(fun):

    def wrapper(num1,num2):

        return fun(abs(num1),abs(num2))
    
    return wrapper

@abs_dec
def add_number(num1,num2):

    return num1 + num2

print(add_number(4,5))




# @property decorator


class Employee:

    def __init__(self,id,name,department):

        self.id = id

        self.name = name

        self.department = department
    @property
    def get_name(self):

        print(self.name)

Employee_instamce =Employee(1,"arun","cs")

Employee_instamce.get_name

print(Employee_instamce.department)