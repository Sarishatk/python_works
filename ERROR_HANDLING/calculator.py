class Calculator:

    def operation(self,*args,**kwargs):

        if kwargs.get("op") == "+":

            return args[0]+args[1]+args[2]
        
        if kwargs.get("op") == "-":

            return args[0]-args[1]-args[2]

       


calculator_instnace = Calculator()

print(calculator_instnace.operation(12,20,30, op = "+"))

print(calculator_instnace.operation(12,20,30, op = "-"))
