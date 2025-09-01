class Book:
    def __init__(self,name,author,price):
        
        self.name = name

        self.author = author

        self.price = price

    def display_book(self):

        print(self.name,self.author,self.price)

book_instance = Book("goat life","biriyani",560)

book_instance.display_book()


class Movie:
    def __init__(self,title,director,language,year):
        
        self.title = title

        self.director = director

        self.language = language

        self.year = year


    def display_movie(self):

        print(self.title,self.director,self.language,self.year)
    
    def __str__(self):

        return self.title

book_instance1 = Movie("swapna kkoode","babu","malayalam",1760)

book_instance1.display_movie()

print(book_instance1)


