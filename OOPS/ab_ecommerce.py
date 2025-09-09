from abc import ABC,abstractmethod

class Ecommerce(ABC):

    @abstractmethod

    def product_list(self):
        pass

    @abstractmethod

    def add_to_cart(self):

        pass

    @abstractmethod

    def cat_summary(self):

        pass
    @abstractmethod


    def place_order(self):

        pass

class Amazon(Ecommerce):

    def product_list(self):

        print("amazon product list")

    def add_to_cart(self):

        print("amazon add to card list")

    def cat_summary(self):

        print("amazon cart summary")

    def place_order(self):

        print("amazon place order")

amazon_instance = Amazon()

amazon_instance.add_to_cart()

