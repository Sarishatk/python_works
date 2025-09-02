class Shape:

    def __int__(self,name,edge_count):

        self.name = name

        self.edge_count = edge_count

    def calculate_area(self):

        print(f"calculating {self.name} area")

class Squre(Shape):
    
    def __init__(self,name,edge_count,s):

        super().__init__(name,edge_count)
        
        self.s = s

    def calculate_area(self):
        
        a = self.s**2

        print(f"area of {self.name} is {a}")

