class Animal:
    def sound(self):
        print("animal sound methode")

# IS method cat is a

class Cat(Animal):
    def sound(self):
        # parent class le sound method vilikkunnu
        super().sound()
        print("cat sound is mwow")

cat_instance = Cat()

cat_instance.sound()