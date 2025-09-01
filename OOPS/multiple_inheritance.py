# child class inherit multiple class



class Father:

    def cricklet_skilss(self):

        print("father cricket skill")

class Mother():

    def cooking_skill(self):

        print("mother cooking skill")

class Child(Father,Mother):

    def play(self):

        print("playing football")

child_instance = Child()

child_instance.cricklet_skilss()

child_instance.cooking_skill()