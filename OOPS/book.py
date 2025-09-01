class Book:
    def __init__(self,name,author,price):
        
        self.name = name

        self.author = author

        self.price = price

    def display_book(self):

        print(self.name,self.author,self.price)

book_instance = Book("goat life","biriyani",560)

book_instance.display_book()

        