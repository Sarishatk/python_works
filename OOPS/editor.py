
from abc import ABC,abstractmethod
class Editior(ABC):

    @abstractmethod

    def open(self):

        pass

    @abstractmethod

    def execute(self):

        pass

    @abstractmethod

    def debug(self):

        pass

class Vscode(Editior):

    def open(self):

        print("vs code open using code .")

    def execute(self):

        print("vs code execute")

    def debug(self):
        
        print("vs code debugging")

vscode_instance = Vscode()

vscode_instance.open()
   