class GrandParent:

    def house(self):

        print("grand parent house")


class Parent(GrandParent):

    def car(self):

        print("parent swift car")

class child(Parent):

    def bike(self):

        print("child bike method")

child_instance = child()

child_instance.car()

child_instance.bike()

child_instance.house()

