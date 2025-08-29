# student (id,name,department ,domain)[set_student(),display_students()]


class Student:

    id:int

    name:str

    department:str

    domain:str

    def set_student(self,id,name,department,domain):

        self.id =  id

        self.name = name

        self.department = department

        self.domain = domain

    def display_student(self):
      
      print(self.id,self.name,self.department,self.domain)

student_instance1 = Student()

student_instance2 = Student()

student_instance1.set_student(1,"dona","CS","AI")

student_instance1.display_student()

student_instance2.set_student(2,"Anagha","CS","ML")

student_instance2.display_student()



