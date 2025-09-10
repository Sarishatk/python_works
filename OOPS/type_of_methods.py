"""
methods are type of function definied inside a class

1)instance method
2)class method
3)static method
"""
class Employee:

    def __init__(self,id,name):

        self.id = id

        self.name = name

    def display_employee(self): 
        # instance method

        print(self.id,self.name)

    @classmethod
    def cls_method_demo(cls):

        print("inside class method")

Employee.cls_method_demo()

        